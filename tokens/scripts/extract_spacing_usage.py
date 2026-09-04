#!/usr/bin/env python3
"""
Extract the real spacing and sizing usage graph from the GSL design system.

Read-only. Emits `spacing-usage-ledger.json` and `spacing-usage-ledger.md` into --out.

Covers two related but distinct scales:

  * `spacing.*` (17) — gaps, padding and margins. A rhythm scale.
  * `sizing.*`  (43) — fixed widths and heights. A dimension scale, and
    currently undocumented.

As with typography, **an unconsumed token is not a dead token**: page-level
rhythm (spacing 48 and above) is applied by product pages outside this
monorepo. The script reports component consumption and says so.

It also mechanically checks the two rules stated in `spacing-tokens.md` that
can be verified from component tokens alone:

  1. Page-rhythm tokens are never used inside a component.
  2. An inner gap never exceeds its container's padding.

Usage:
    python3 extract_spacing_usage.py --code-repo /path/to/gsl-core-web-design-system
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

PAGE_RHYTHM = {"48", "56", "64", "80", "128", "256"}
REF_RE = re.compile(r"^\{((?:spacing|sizing)\.[A-Za-z0-9_.]+)\}$")
CODE_RE = re.compile(r'["\'`]((?:spacing|sizing)\.[A-Za-z0-9_.]+)')
SKIP_SUFFIX = ("test.ts", "test.tsx", "stories.ts", "stories.tsx")
SKIP_PATH = ("/stories/", "/__tests__/", "/dist/", "/node_modules/")


def leaves(node, prefix=""):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        yield prefix, node["$value"]
        return
    for key, child in node.items():
        yield from leaves(child, f"{prefix}.{key}" if prefix else key)


def load_scales(tokens_src: Path):
    spacing = dict(leaves(json.loads((tokens_src / "shared" / "figma" / "spacings.json").read_text())))
    sizing = dict(leaves(json.loads((tokens_src / "shared" / "sizings.json").read_text())))
    return spacing, sizing


def load_component_usage(tokens_src: Path):
    usage = defaultdict(list)
    per_file = {}
    for f in sorted((tokens_src / "shared" / "components").glob("*.json")):
        flat = dict(leaves(json.loads(f.read_text())))
        per_file[f.stem] = flat
        for path, value in flat.items():
            if not isinstance(value, str):
                continue
            m = REF_RE.match(value)
            if m:
                usage[m.group(1)].append({"component": f.stem, "component_token": path})
    return usage, per_file


def load_direct_usage(repo: Path):
    direct = defaultdict(set)
    for base in sorted((repo / "libraries").glob("*/src")):
        for f in sorted(list(base.rglob("*.ts")) + list(base.rglob("*.tsx"))):
            rel = str(f.relative_to(repo))
            if any(s in f"/{rel}" for s in SKIP_PATH) or rel.endswith(SKIP_SUFFIX):
                continue
            owner = rel.split("/src/", 1)[1].split("/")[0] if "/src/" in rel else "?"
            for m in CODE_RE.findall(f.read_text(errors="ignore")):
                direct[m.rstrip(".")].add(owner)
    return direct


def check_rules(per_file: dict, spacing: dict):
    """The two rules from spacing-tokens.md that component tokens can verify."""
    rhythm = []
    for comp, flat in per_file.items():
        for path, value in flat.items():
            m = REF_RE.match(value) if isinstance(value, str) else None
            if m and m.group(1).startswith("spacing."):
                leaf = m.group(1).split(".", 1)[1]
                if leaf in PAGE_RHYTHM:
                    rhythm.append({"component": comp, "component_token": path,
                                   "token": m.group(1)})

    containment, checked = [], []
    for comp, flat in per_file.items():
        def px(path, value):
            m = REF_RE.match(value) if isinstance(value, str) else None
            if not m or not m.group(1).startswith("spacing."):
                return None
            return spacing.get(m.group(1))

        # `margin.*` is spacing *outside* the container; it is not an inner gap
        pads = [px(p, v) for p, v in flat.items()
                if "padding" in p.lower() and ".margin." not in p]
        gaps = [(p, px(p, v)) for p, v in flat.items()
                if "gap" in p.lower() and ".margin." not in p]
        pads = [x for x in pads if x is not None]
        gaps = [(p, g) for p, g in gaps if g is not None]
        if not pads or not gaps:
            continue
        checked.append(comp)
        widest = max(pads)
        for path, gap in gaps:
            if gap > widest:
                containment.append({"component": comp, "component_token": path,
                                    "gap": gap, "max_padding": widest})
    return {
        "page_rhythm_violations": rhythm,
        "containment_violations": containment,
        "containment_components_checked": sorted(checked),
    }


def build(repo: Path):
    tokens_src = repo / "libraries" / "tokens" / "src"
    spacing, sizing = load_scales(tokens_src)
    usage, per_file = load_component_usage(tokens_src)
    direct = load_direct_usage(repo)

    def ledger(scale):
        out = {}
        for token, value in scale.items():
            binds = usage.get(token, [])
            code = sorted(direct.get(token, set()))
            out[token] = {
                "token": token,
                "value": value,
                "component_consumers": sorted({b["component"] for b in binds}),
                "binding_count": len(binds),
                "bindings": binds,
                "direct_code_owners": code,
                "no_component_consumer": not binds and not code,
            }
        return out

    sp, sz = ledger(spacing), ledger(sizing)
    return {
        "meta": {
            "code_repo": str(repo),
            "spacing_token_count": len(sp),
            "sizing_token_count": len(sz),
            "spacing_binding_count": sum(v["binding_count"] for v in sp.values()),
            "sizing_binding_count": sum(v["binding_count"] for v in sz.values()),
            "spacing_unconsumed": sorted(t for t, v in sp.items() if v["no_component_consumer"]),
            "sizing_unconsumed": sorted(t for t, v in sz.items() if v["no_component_consumer"]),
        },
        "rules": check_rules(per_file, spacing),
        "spacing": sp,
        "sizing": sz,
    }


def render(L: dict) -> str:
    m, r = L["meta"], L["rules"]
    out: list[str] = []
    w = out.append

    w("# Spacing and sizing usage ledger (generated)\n")
    w("_Generated by `scripts/extract_spacing_usage.py`. Do not edit by hand._\n")
    w("> **An unconsumed token is not a dead token.** Page-level rhythm "
      "(`spacing/48` and above) is applied by product pages outside this "
      "monorepo. This ledger reports **component** consumption only.\n")

    w("## Summary\n")
    w("| Metric | Value |")
    w("| --- | --- |")
    w(f"| `spacing.*` tokens | {m['spacing_token_count']} |")
    w(f"| `spacing.*` component bindings | {m['spacing_binding_count']} |")
    w(f"| `spacing.*` with no component consumer | {len(m['spacing_unconsumed'])} |")
    w(f"| `sizing.*` tokens | {m['sizing_token_count']} |")
    w(f"| `sizing.*` component bindings | {m['sizing_binding_count']} |")
    w(f"| `sizing.*` with no component consumer | {len(m['sizing_unconsumed'])} |")
    w("")

    w("## Documented rules — mechanical check\n")
    w("| Rule | Result |")
    w("| --- | --- |")
    pr = r["page_rhythm_violations"]
    cv = r["containment_violations"]
    w(f"| Page-rhythm tokens (48+) never used inside a component | "
      f"{'**holds** — 0 violations' if not pr else f'**{len(pr)} violations**'} |")
    w(f"| An inner gap never exceeds its container padding | "
      f"{'**holds** — 0 violations across ' + str(len(r['containment_components_checked'])) + ' components' if not cv else f'**{len(cv)} violations**'} |")
    w("")
    for label, rows in (("Page-rhythm", pr), ("Containment", cv)):
        if rows:
            w(f"### {label} violations\n")
            for x in rows:
                w(f"- `{x['component']}` — `{x['component_token']}`")
            w("")

    for name, key in (("Spacing", "spacing"), ("Sizing", "sizing")):
        w(f"## {name}\n")
        w("| Token | px | Components | Bound by | Direct in code |")
        w("| --- | --- | --- | --- | --- |")
        def order(t):
            leaf = t.split(".", 1)[1]
            return int(leaf) if leaf.isdigit() else -1
        for t in sorted(L[key], key=order):
            v = L[key][t]
            comps = ", ".join(f"`{c}`" for c in v["component_consumers"][:6])
            if len(v["component_consumers"]) > 6:
                comps += f" +{len(v['component_consumers']) - 6}"
            direct = ", ".join(f"`{d}`" for d in v["direct_code_owners"][:3]) or "—"
            w(f"| `{t}` | {v['value']} | {len(v['component_consumers'])} | {comps or '—'} | {direct} |")
        w("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--code-repo", required=True, type=Path)
    ap.add_argument("--out", type=Path,
                    default=Path(__file__).resolve().parent.parent / "spacing")
    a = ap.parse_args()
    repo = a.code_repo.resolve()
    if not (repo / "libraries" / "tokens" / "src").exists():
        raise SystemExit(f"not a design-system repo: {repo}")

    L = build(repo)
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "spacing-usage-ledger.json").write_text(json.dumps(L, indent=2) + "\n")
    (a.out / "spacing-usage-ledger.md").write_text(render(L))
    m, r = L["meta"], L["rules"]
    print(f"spacing : {m['spacing_token_count']} tokens, {m['spacing_binding_count']} bindings, "
          f"{len(m['spacing_unconsumed'])} unconsumed")
    print(f"sizing  : {m['sizing_token_count']} tokens, {m['sizing_binding_count']} bindings, "
          f"{len(m['sizing_unconsumed'])} unconsumed")
    print(f"rules   : page-rhythm {len(r['page_rhythm_violations'])} violations, "
          f"containment {len(r['containment_violations'])} violations")
    print(f"-> {a.out}/spacing-usage-ledger.md")


if __name__ == "__main__":
    main()
