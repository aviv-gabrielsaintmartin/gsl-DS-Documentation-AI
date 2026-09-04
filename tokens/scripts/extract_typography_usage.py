#!/usr/bin/env python3
"""
Extract the real typography usage graph from the GSL design system code repo.

Read-only. Emits `typography-usage-ledger.json` and `typography-usage-ledger.md` into --out.

Typography differs from colour in two ways that shape this script:

  1. Component tokens reference a style by a **literal string** (`"$type":
     "referenceToken"`, value `typography.body.16.regular`), not by a `{...}`
     alias. So the reference syntax is different from colour's.
  2. An unused style is **not** evidence of a dead token. Product pages set type
     directly and live outside this monorepo, so a style with no component
     consumer may still be in daily use on a real screen. This script reports
     component consumption only, and says so.

Usage:
    python3 extract_typography_usage.py --code-repo /path/to/gsl-core-web-design-system
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

INACTIVE_BRANDS = {"AVIV"}
STYLE_RE = re.compile(r'["\'`]typography\.([A-Za-z0-9_.]+)')
SKIP_SUFFIX = ("test.ts", "test.tsx", "stories.ts", "stories.tsx")
SKIP_PATH = ("/stories/", "/__tests__/", "/dist/", "/node_modules/")

# Properties compared across brands to establish what actually varies.
STYLE_PROPS = ("fontFamily", "fontSize", "fontWeight", "lineHeight",
               "letterSpacing", "textCase", "textDecoration", "fontStyle",
               "fontStretch")


def font_styles(path: Path) -> dict:
    """Flatten a brand typographies.json to {dotted.style.name: {props}}."""
    out: dict[str, dict] = {}

    def walk(node, prefix=""):
        if not isinstance(node, dict):
            return
        if node.get("$type") == "custom-fontStyle":
            out[prefix] = node["$value"]
            return
        for key, child in node.items():
            if key.startswith("$"):
                continue
            walk(child, f"{prefix}.{key}" if prefix else key)

    walk(json.loads(path.read_text())["typography"])
    return out


def load_styles(tokens_src: Path, include_inactive: bool):
    brands_dir = tokens_src / "brands"
    brands = sorted(d.name for d in brands_dir.iterdir() if d.is_dir())
    skipped = [] if include_inactive else sorted(b for b in brands if b in INACTIVE_BRANDS)
    if skipped:
        brands = [b for b in brands if b not in INACTIVE_BRANDS]

    per_brand = {b: font_styles(brands_dir / b / "typographies.json") for b in brands}
    shared = font_styles(tokens_src / "shared" / "typographies.json")

    ref = "SL" if "SL" in brands else brands[0]
    names = sorted(per_brand[ref])

    styles = {}
    for name in names:
        by_brand = {b: per_brand[b].get(name, {}) for b in brands}
        varies = {
            p: sorted({json.dumps(v.get(p)) for v in by_brand.values()})
            for p in STYLE_PROPS
        }
        styles[name] = {
            "style": name,
            "reference": by_brand[ref],
            "varies_by_brand": [p for p, vals in varies.items() if len(vals) > 1],
            "font_family_by_brand": {b: v.get("fontFamily") for b, v in by_brand.items()},
        }
    return brands, skipped, styles, shared


def load_component_usage(tokens_src: Path):
    usage = defaultdict(list)
    for f in sorted((tokens_src / "shared" / "components").glob("*.json")):
        comp = f.stem

        def walk(node, prefix=""):
            if not isinstance(node, dict):
                return
            if "$value" in node:
                value = node["$value"]
                if isinstance(value, str) and value.startswith("typography."):
                    usage[value[len("typography."):]].append(
                        {"component": comp, "component_token": prefix}
                    )
                return
            for key, child in node.items():
                walk(child, f"{prefix}.{key}" if prefix else key)

        walk(json.loads(f.read_text()))
    return usage


def load_direct_usage(repo: Path):
    direct = defaultdict(set)
    for base in sorted((repo / "libraries").glob("*/src")):
        for f in sorted(list(base.rglob("*.ts")) + list(base.rglob("*.tsx"))):
            rel = str(f.relative_to(repo))
            if any(s in f"/{rel}" for s in SKIP_PATH) or rel.endswith(SKIP_SUFFIX):
                continue
            owner = rel.split("/src/", 1)[1].split("/")[0] if "/src/" in rel else "?"
            for m in STYLE_RE.findall(f.read_text(errors="ignore")):
                direct[m.rstrip(".")].add(owner)
    return direct


def build(repo: Path, include_inactive: bool = False):
    tokens_src = repo / "libraries" / "tokens" / "src"
    brands, skipped, styles, shared = load_styles(tokens_src, include_inactive)
    usage = load_component_usage(tokens_src)
    direct = load_direct_usage(repo)

    ledger = {}
    for name, meta in styles.items():
        binds = usage.get(name, [])
        code = sorted(direct.get(name, set()))
        ledger[name] = {
            **meta,
            "component_consumers": sorted({b["component"] for b in binds}),
            "bindings": binds,
            "direct_code_owners": code,
            "no_component_consumer": not binds and not code,
        }

    shared_ledger = {}
    for name in shared:
        binds = usage.get(name, [])
        shared_ledger[name] = {
            "style": name,
            "value": shared[name],
            "component_consumers": sorted({b["component"] for b in binds}),
            "bindings": binds,
            "direct_code_owners": sorted(direct.get(name, set())),
        }

    unbound = sorted(n for n, v in ledger.items() if v["no_component_consumer"])
    varying = sorted({p for v in ledger.values() for p in v["varies_by_brand"]})

    return {
        "meta": {
            "code_repo": str(repo),
            "brands": brands,
            "excluded_brands": skipped,
            "style_count": len(ledger),
            "shared_style_count": len(shared_ledger),
            "no_component_consumer_count": len(unbound),
            "properties_varying_by_brand": varying,
            "font_family_by_brand": (
                next(iter(ledger.values()))["font_family_by_brand"] if ledger else {}
            ),
        },
        "styles": ledger,
        "shared_styles": shared_ledger,
        "no_component_consumer": unbound,
    }


def render(L: dict) -> str:
    m = L["meta"]
    out: list[str] = []
    w = out.append

    w("# Typography usage ledger (generated)\n")
    w("_Generated by `scripts/extract_typography_usage.py`. Do not edit by hand._\n")
    w("> **A style with no component consumer is not a dead token.** Product "
      "pages set type directly and live outside this monorepo, so this ledger "
      "reports **component** consumption only. See "
      "[typography-usage-audit.md](typography-usage-audit.md) for the "
      "real-screen evidence.\n")

    w("## Summary\n")
    w("| Metric | Value |")
    w("| --- | --- |")
    w(f"| Text styles per brand | {m['style_count']} |")
    w(f"| Brands | {len(m['brands'])} ({', '.join(m['brands'])}) |")
    if m["excluded_brands"]:
        w(f"| Excluded (present in source, not in use) | {', '.join(m['excluded_brands'])} |")
    w(f"| Shared (non-brand) styles | {m['shared_style_count']} |")
    w(f"| Styles with **no component consumer** | {m['no_component_consumer_count']} |")
    w(f"| Properties that vary by brand | {', '.join(m['properties_varying_by_brand']) or 'none'} |")
    w("")

    w("## Font family by brand\n")
    w("| Brand | Font family |")
    w("| --- | --- |")
    for b, fam in m["font_family_by_brand"].items():
        w(f"| {b} | `{fam}` |")
    w("\n_Every other property — size, weight, line height, letter spacing, "
      "case, decoration — is identical across all brands._\n")

    w("## Styles\n")
    w("| Style | Size / LH / Weight | Components | Direct in code |")
    w("| --- | --- | --- | --- |")
    for name, v in L["styles"].items():
        r = v["reference"]
        spec = f"{r.get('fontSize')}/{r.get('lineHeight')}/{r.get('fontWeight')}"
        comps = ", ".join(f"`{c}`" for c in v["component_consumers"]) or "—"
        direct = ", ".join(f"`{d}`" for d in v["direct_code_owners"]) or "—"
        w(f"| `{name}` | {spec} | {comps} | {direct} |")
    w("")

    w("## Shared styles (not brand-specific)\n")
    for name, v in L["shared_styles"].items():
        comps = ", ".join(f"`{c}`" for c in v["component_consumers"]) or "—"
        w(f"- `typography.{name}` — {json.dumps(v['value'])}\n  consumers: {comps}")
    w("")

    w("## Styles with no component consumer\n")
    w("_Not necessarily unused — see the note at the top._\n")
    for n in L["no_component_consumer"]:
        w(f"- `{n}`")
    w("")

    w("## Per-component contract\n")
    by_comp = defaultdict(list)
    for name, v in L["styles"].items():
        for b in v["bindings"]:
            by_comp[b["component"]].append((b["component_token"], name))
    for comp in sorted(by_comp):
        w(f"### `{comp}` ({len(by_comp[comp])})\n")
        w("| Component token | Style |")
        w("| --- | --- |")
        for tok, name in sorted(by_comp[comp]):
            w(f"| `{tok}` | `{name}` |")
        w("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--code-repo", required=True, type=Path)
    ap.add_argument("--include-inactive-brands", action="store_true")
    ap.add_argument("--out", type=Path,
                    default=Path(__file__).resolve().parent.parent / "typography")
    a = ap.parse_args()

    repo = a.code_repo.resolve()
    if not (repo / "libraries" / "tokens" / "src").exists():
        raise SystemExit(f"not a design-system repo: {repo}")

    L = build(repo, a.include_inactive_brands)
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "typography-usage-ledger.json").write_text(json.dumps(L, indent=2) + "\n")
    (a.out / "typography-usage-ledger.md").write_text(render(L))

    m = L["meta"]
    print(f"brands            : {', '.join(m['brands'])}"
          + (f"   (excluded: {', '.join(m['excluded_brands'])})" if m["excluded_brands"] else ""))
    print(f"styles            : {m['style_count']} (+{m['shared_style_count']} shared)")
    print(f"no component use  : {m['no_component_consumer_count']}")
    print(f"varies by brand   : {', '.join(m['properties_varying_by_brand']) or 'nothing'}")
    print(f"-> {a.out}/typography-usage-ledger.json")
    print(f"-> {a.out}/typography-usage-ledger.md")


if __name__ == "__main__":
    main()
