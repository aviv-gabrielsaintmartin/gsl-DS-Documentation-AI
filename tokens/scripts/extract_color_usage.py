#!/usr/bin/env python3
"""
Extract the real color-token usage graph from the GSL design system code repo.

Reads only. Emits `color-usage-ledger.json` (machine-readable ledger) and
`color-usage-ledger.md` (human-readable rendering) into --out.

Three sources are read:
  1. brands/<BRAND>/figma/colors.{light,dark}.json  -> the semantic color set
  2. shared/components/*.json                       -> component-token bindings
  3. libraries/{ui,patterns,core}/src/**.{ts,tsx}   -> direct usage (bypasses)

Nothing here makes a judgement about whether a binding is correct. It records
what is bound to what, and flags the mismatches for human adjudication.

Usage:
    python3 extract_color_usage.py --code-repo /path/to/gsl-core-web-design-system
"""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

# --------------------------------------------------------------------------
# Vocabulary
#
# Derived from the actual leaf names in shared/components/*.json, not invented.
# Any word not listed here is reported under `unclassified_words` rather than
# silently guessed at.
# --------------------------------------------------------------------------

ROLE_WORDS = {
    # Only words that genuinely name a *paint role*. Element nouns (knob,
    # track, indicator, overlay, star, dot...) are deliberately NOT listed:
    # guessing their role produces false mismatches. A leaf with no role word
    # is recorded as role "unknown" and excluded from mismatch detection.
    "bg": "surface", "background": "surface",
    "border": "border", "outline": "border", "stroke": "border",
    "divider": "border", "separator": "border",
    "text": "content", "content": "content", "label": "content",
    "placeholder": "content", "description": "content", "helper": "content",
    "title": "content", "subtitle": "content", "caption": "content",
    "message": "content", "optional": "content",
    "icon": "icon", "symbol": "icon",
    "shadow": "shadow",
}

STATE_WORDS = {
    "default", "hover", "hovered", "pressed", "active", "focus", "focused",
    "selected", "checked", "disabled", "loading", "open", "opened",
    "expanded", "collapsed", "current", "visited", "empty", "filled",
    "readonly", "dragging", "complete", "completed", "todo",
}

STATUS_WORDS = {
    "error", "success", "warning", "information", "info", "danger",
    "critical", "neutral", "positive", "negative",
}

# Which semantic families are coherent for a given role. A binding whose
# family is not in this set is surfaced as a role/family mismatch — the
# highest-signal delta this script produces.
ROLE_EXPECTED_FAMILIES = {
    "surface": {"surface", "background", "scales"},
    "border":  {"border", "scales"},
    "content": {"content", "scales", "symbol"},
    "icon":    {"symbol", "content", "scales"},
    "shadow":  set(),
}

# Brands whose token set ships in the source tree but is not a live product.
# Excluded from the ledger so counts and brand-variance reflect real brands.
# Override with --include-inactive-brands.
INACTIVE_BRANDS = {"AVIV"}

CAMEL_RE = re.compile(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])")
# `color.x.y` not preceded by a dot/word char, so `toggle.color.content` (a
# component-token path) does not match as a semantic-token reference.
SEMANTIC_IN_CODE_RE = re.compile(r"(?<![A-Za-z0-9_.])color\.[a-z][A-Za-z0-9_.]*")
REF_RE = re.compile(r"^\{(.+)\}$")


# --------------------------------------------------------------------------
# Generic helpers
# --------------------------------------------------------------------------

def leaves(node, prefix=""):
    """Yield (dotted-path, $value) for every token leaf in a DTCG-ish tree."""
    if not isinstance(node, dict):
        return
    if "$value" in node:
        yield prefix, node["$value"]
        return
    for key, child in node.items():
        yield from leaves(child, f"{prefix}.{key}" if prefix else key)


def split_camel(word: str) -> list[str]:
    return [w.lower() for w in CAMEL_RE.findall(word)]


def hex_to_rgba(value: str):
    """#rrggbb or #rrggbbaa -> (r, g, b, alpha 0..1). None if unparseable."""
    v = value.strip().lstrip("#")
    if len(v) == 6:
        return int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16), 1.0
    if len(v) == 8:
        return int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16), int(v[6:8], 16) / 255
    return None


def relative_luminance(rgb) -> float:
    def channel(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg_hex: str, bg_hex: str):
    """WCAG ratio. Returns None when either colour carries alpha, because the
    true composite depends on what sits behind it."""
    fg, bg = hex_to_rgba(fg_hex), hex_to_rgba(bg_hex)
    if not fg or not bg or fg[3] < 1.0 or bg[3] < 1.0:
        return None
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return round((hi + 0.05) / (lo + 0.05), 2)


# --------------------------------------------------------------------------
# Source 1 — the semantic color set
# --------------------------------------------------------------------------

def load_semantic_tokens(tokens_src: Path, include_inactive: bool = False):
    brands_dir = tokens_src / "brands"
    brands = sorted(d.name for d in brands_dir.iterdir() if d.is_dir())
    skipped = [] if include_inactive else sorted(b for b in brands if b in INACTIVE_BRANDS)
    if skipped:
        brands = [b for b in brands if b not in INACTIVE_BRANDS]

    values = {}  # (brand, mode) -> {token: hex}
    for brand in brands:
        for mode in ("light", "dark"):
            path = brands_dir / brand / "figma" / f"colors.{mode}.json"
            values[(brand, mode)] = dict(leaves(json.loads(path.read_text())))

    all_keys = sorted({k for v in values.values() for k in v})

    tokens = {}
    for key in all_keys:
        family = key.split(".")[1] if key.startswith("color.") else "?"
        per_mode = {}
        for mode in ("light", "dark"):
            per_brand = {b: values[(b, mode)].get(key) for b in brands}
            distinct = sorted({v for v in per_brand.values() if v is not None})
            per_mode[mode] = {
                "by_brand": per_brand,
                "distinct_values": len(distinct),
                "varies_by_brand": len(distinct) > 1,
            }
        has_alpha = any(
            (v or "").startswith("#") and len(v) == 9
            for m in per_mode.values() for v in m["by_brand"].values()
        )
        tokens[key] = {
            "token": key,
            "family": family,
            "has_alpha": has_alpha,
            "modes": per_mode,
        }
    return brands, tokens, skipped


# --------------------------------------------------------------------------
# Source 2 — component-token bindings
# --------------------------------------------------------------------------

def parse_binding_path(path: str):
    """`component.toggle.color.borderHover` -> role/state/status/variant."""
    parts = path.split(".")
    component = parts[1] if len(parts) > 1 else "?"

    try:
        color_idx = next(i for i, p in enumerate(parts) if p == "color" and i >= 2)
        after = parts[color_idx + 1:]
    except StopIteration:
        after = []

    if not after:  # e.g. `component.divider.color` — a scalar, no role in name
        return component, "", "", "unspecified", "default", None, []

    variant = ".".join(after[:-1])
    leaf = after[-1]

    words = split_camel(leaf)
    # variant segments carry status/state qualifiers too (e.g. `success.bg`)
    context = [w for seg in after[:-1] for w in split_camel(seg)]

    # Last role word wins: in `overlayText` the paint role is the text, not
    # the overlay it sits on; in `borderHover` there is only one candidate.
    role = "unknown"
    for w in words:
        if w in ROLE_WORDS:
            role = ROLE_WORDS[w]

    states = [w for w in words + context if w in STATE_WORDS]
    statuses = [w for w in words + context if w in STATUS_WORDS]
    unclassified = [
        w for w in words
        if w not in ROLE_WORDS and w not in STATE_WORDS and w not in STATUS_WORDS
    ]

    state = states[0] if states else "default"
    status = statuses[0] if statuses else None
    return component, variant, leaf, role, state, status, unclassified


def load_component_bindings(tokens_src: Path):
    comp_dir = tokens_src / "shared" / "components"
    bindings = []
    unclassified = Counter()
    all_files = sorted(f.name for f in comp_dir.glob("*.json"))

    for f in sorted(comp_dir.glob("*.json")):
        tree = json.loads(f.read_text())
        for path, value in leaves(tree):
            if not isinstance(value, str):
                continue
            m = REF_RE.match(value)
            if not m or not m.group(1).startswith("color."):
                continue
            semantic = m.group(1)
            component, variant, leaf, role, state, status, unk = parse_binding_path(path)
            for w in unk:
                unclassified[w] += 1
            bindings.append({
                "component": component,
                "file": f"shared/components/{f.name}",
                "component_token": path,
                "variant": variant,
                "leaf": leaf,
                "role": role,
                "state": state,
                "status": status,
                "semantic_token": semantic,
                "semantic_family": semantic.split(".")[1],
            })
    coloured = {b["file"].split("/")[-1] for b in bindings}
    colourless = [f for f in all_files if f not in coloured]
    return bindings, unclassified, colourless


# --------------------------------------------------------------------------
# Source 3 — direct semantic usage in component code (bypasses)
# --------------------------------------------------------------------------

def load_direct_usage(repo: Path, defined: set[str]):
    roots = sorted(str(p.relative_to(repo)) for p in (repo / "libraries").glob("*/src"))
    skip = ("/stories/", "/__tests__/", "/dist/", "/node_modules/")

    direct = defaultdict(list)
    dynamic = defaultdict(list)

    for root in roots:
        base = repo / root
        for f in sorted(list(base.rglob("*.ts")) + list(base.rglob("*.tsx"))):
            rel = str(f.relative_to(repo))
            if any(s in f"/{rel}" for s in skip) or rel.endswith(
                ("test.ts", "test.tsx", "stories.ts", "stories.tsx")
            ):
                continue
            owner = rel.split("/src/", 1)[1].split("/")[0] if "/src/" in rel else "?"
            for match in SEMANTIC_IN_CODE_RE.findall(f.read_text(errors="ignore")):
                token = match.rstrip(".")
                entry = {"file": rel, "owner": owner}
                if match.endswith(".") or token not in defined:
                    # template-literal prefix like `color.content.${...}`
                    dynamic[match].append(entry)
                else:
                    direct[token].append(entry)
    return direct, dynamic


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------

def build_ledger(repo: Path, include_inactive: bool = False):
    tokens_src = repo / "libraries" / "tokens" / "src"
    brands, semantic, skipped_brands = load_semantic_tokens(tokens_src, include_inactive)
    bindings, unclassified, colourless = load_component_bindings(tokens_src)
    direct, dynamic = load_direct_usage(repo, set(semantic))

    by_token = defaultdict(list)
    for b in bindings:
        by_token[b["semantic_token"]].append(b)

    # A template literal like `color.surface.data.${entry.color}` really does
    # consume every token under that prefix. A permissive prop type such as
    # `color.surface.${string}` does not — it only declares what the prop will
    # accept. Distinguish by specificity: a prefix must name a family *and* a
    # sub-group before we treat it as evidence of consumption.
    dynamic_hits = defaultdict(list)
    wildcard_prefixes = {}
    for prefix, uses in dynamic.items():
        stem = prefix.rstrip(".") + "."
        segments = [p for p in stem.split(".") if p][1:]  # drop leading "color"
        if len(segments) < 2:
            wildcard_prefixes[prefix] = uses
            continue
        for token in semantic:
            if token.startswith(stem):
                dynamic_hits[token].extend(uses)

    ledger = {}
    for token, meta in semantic.items():
        consumers = by_token.get(token, [])
        code_uses = direct.get(token, [])
        dyn_uses = dynamic_hits.get(token, [])
        roles = sorted({c["role"] for c in consumers})
        mismatches = [
            c for c in consumers
            if c["role"] in ROLE_EXPECTED_FAMILIES
            and c["semantic_family"] not in ROLE_EXPECTED_FAMILIES[c["role"]]
        ]
        ledger[token] = {
            **meta,
            "component_consumers": sorted({c["component"] for c in consumers}),
            "binding_count": len(consumers),
            "roles": roles,
            "states": sorted({c["state"] for c in consumers}),
            "bindings": consumers,
            "direct_code_uses": code_uses,
            "direct_code_owners": sorted({u["owner"] for u in code_uses}),
            "dynamic_code_uses": dyn_uses,
            "dynamic_code_owners": sorted({u["owner"] for u in dyn_uses}),
            "is_orphan": not consumers and not code_uses and not dyn_uses,
            "role_family_mismatches": mismatches,
        }

    # role x state -> which semantic tokens serve it (consistency view)
    role_state = defaultdict(lambda: defaultdict(list))
    for b in bindings:
        key = f"{b['role']}/{b['status'] + '/' if b['status'] else ''}{b['state']}"
        role_state[key][b["semantic_token"]].append(b["component"])

    # per-component contract
    components = defaultdict(list)
    for b in bindings:
        components[b["component"]].append(b)

    # Tokens that resolve to the SAME value in light mode but DIFFERENT values in
    # dark. Picking the wrong one of a colliding group is invisible in light mode
    # and breaks in dark — the failure mode behind the inverted-Link bug.
    # SL is the reference brand used throughout the docs.
    ref = "SL" if "SL" in brands else (brands[0] if brands else None)
    by_light = defaultdict(list)
    for token, meta in semantic.items():
        by_light[meta["modes"]["light"]["by_brand"].get(ref)].append(token)
    collisions = []
    for light_value, toks in by_light.items():
        if len(toks) < 2:
            continue
        darks = {t: semantic[t]["modes"]["dark"]["by_brand"].get(ref) for t in toks}
        if len(set(darks.values())) < 2:
            continue
        collisions.append({
            "light_value": light_value,
            "dark_values": len(set(darks.values())),
            "tokens": [
                {
                    "token": t,
                    "dark": darks[t],
                    "consumers": len(by_token.get(t, [])) + len(direct.get(t, [])),
                }
                for t in sorted(toks)
            ],
        })
    collisions.sort(key=lambda c: -len(c["tokens"]))

    orphans = sorted(t for t, v in ledger.items() if v["is_orphan"])
    dynamic_only = sorted(t for t, v in ledger.items()
                          if v["dynamic_code_uses"] and not v["bindings"] and not v["direct_code_uses"])
    mismatches = [m for v in ledger.values() for m in v["role_family_mismatches"]]

    return {
        "meta": {
            "code_repo": str(repo),
            "brands": brands,
            "excluded_brands": skipped_brands,
            "semantic_token_count": len(semantic),
            "component_file_count": len({b["file"] for b in bindings}),
            "binding_count": len(bindings),
            "orphan_count": len(orphans),
            "direct_usage_count": len(direct),
            "dynamic_only_count": len(dynamic_only),
            "role_family_mismatch_count": len(mismatches),
            "light_mode_collision_count": len(collisions),
            "unclassified_leaf_words": dict(unclassified.most_common()),
            "component_files_without_color": colourless,
        },
        "tokens": ledger,
        "components": {k: sorted(v, key=lambda x: x["component_token"])
                       for k, v in sorted(components.items())},
        "role_state_index": {k: {t: sorted(set(c)) for t, c in sorted(v.items())}
                             for k, v in sorted(role_state.items())},
        "light_mode_collisions": collisions,
        "orphans": orphans,
        "dynamic_only_tokens": dynamic_only,
        "role_family_mismatches": mismatches,
        "direct_usage": {k: sorted({u["owner"] for u in v}) for k, v in sorted(direct.items())},
        "dynamic_usage": {k: sorted({u["file"] for u in v}) for k, v in sorted(dynamic.items())},
        "wildcard_prop_types": {k: sorted({u["file"] for u in v})
                                for k, v in sorted(wildcard_prefixes.items())},
    }


# --------------------------------------------------------------------------
# Markdown rendering
# --------------------------------------------------------------------------

def render_markdown(L: dict) -> str:
    m = L["meta"]
    out: list[str] = []
    w = out.append

    w("# Color usage ledger (generated)\n")
    w("_Generated by `scripts/extract_color_usage.py`. Do not edit by hand — "
      "re-run the script. This file records **what is bound to what**; it makes "
      "no judgement about whether a binding is correct. Adjudication lives in "
      "[color-usage-audit.md](color-usage-audit.md)._\n")

    w("## Summary\n")
    w("| Metric | Value |")
    w("| --- | --- |")
    w(f"| Semantic color tokens defined | {m['semantic_token_count']} |")
    w(f"| Brands × modes | {len(m['brands'])} × 2 ({', '.join(m['brands'])}) |")
    if m["excluded_brands"]:
        w(f"| Brands excluded (present in source, not in use) | {', '.join(m['excluded_brands'])} |")
    w(f"| Component token files | {m['component_file_count']} |")
    w(f"| Component → semantic bindings | {m['binding_count']} |")
    w(f"| Tokens with **no consumer** | {m['orphan_count']} "
      f"({round(100 * m['orphan_count'] / m['semantic_token_count'])}%) |")
    w(f"| Tokens used **directly in code** (bypassing the component tier) | {m['direct_usage_count']} |")
    w(f"| Role/family mismatches | {m['role_family_mismatch_count']} |")
    w("")

    w("## Role / family mismatches\n")
    w("_A binding whose component-token role disagrees with the semantic family "
      "it points at — e.g. a `border` role bound to a `surface` token._\n")
    if L["role_family_mismatches"]:
        w("| Component | Component token | Role | Semantic token | Family |")
        w("| --- | --- | --- | --- | --- |")
        for x in sorted(L["role_family_mismatches"], key=lambda x: x["component_token"]):
            w(f"| `{x['component']}` | `{x['component_token']}` | {x['role']} "
              f"| `{x['semantic_token']}` | {x['semantic_family']} |")
    else:
        w("_None found._")
    w("")

    w("## Role × state consistency\n")
    w("_For each role+state, which semantic tokens serve it. More than one row "
      "per role/state is not automatically wrong (status variants are "
      "legitimate) — it is where to look for drift._\n")
    for key, tokens in L["role_state_index"].items():
        if len(tokens) < 2:
            continue
        w(f"### `{key}`\n")
        w("| Semantic token | Components |")
        w("| --- | --- |")
        for tok, comps in sorted(tokens.items(), key=lambda x: -len(x[1])):
            w(f"| `{tok}` | {len(comps)} — {', '.join(f'`{c}`' for c in comps)} |")
        w("")

    w("## Direct usage — component-tier bypasses\n")
    w("_Semantic tokens referenced straight from `.tsx`/`.ts`, skipping the "
      "`unsafe_component.*` tier._\n")
    w("| Semantic token | Owners |")
    w("| --- | --- |")
    for tok, owners in sorted(L["direct_usage"].items(), key=lambda x: (-len(x[1]), x[0])):
        w(f"| `{tok}` | {', '.join(f'`{o}`' for o in owners)} |")
    w("")
    if L["wildcard_prop_types"]:
        w("### Permissive prop types\n")
        w("_Public props typed to accept **any** token in a family. They are not "
          "evidence that a given token is used, but they are a hole in the "
          "system: a consumer can pass anything the family contains._\n")
        for prefix, files in L["wildcard_prop_types"].items():
            w(f"- `{prefix}${{string}}` — {', '.join(f'`{f}`' for f in files)}")
        w("")

    w("## Light-mode collisions\n")
    w("_Tokens that resolve to the **same** value in light mode but **different** "
      "values in dark. Picking the wrong one of a group is invisible in light "
      "mode and breaks in dark — audit these hardest against Figma. `consumers` "
      "counts live component bindings plus direct code use._\n")
    for c in L["light_mode_collisions"]:
        w(f"### `{c['light_value']}` — {len(c['tokens'])} tokens, "
          f"{c['dark_values']} different dark values\n")
        w("| Token | Dark | Consumers |")
        w("| --- | --- | --- |")
        for t in c["tokens"]:
            w(f"| `{t['token']}` | `{t['dark']}` | {t['consumers']} |")
        w("")

    w("## Tokens consumed only dynamically\n")
    w("_Referenced through a template literal, so no single call site names "
      "them. Real usage — not orphans._\n")
    for t in L["dynamic_only_tokens"]:
        w(f"- `{t}` — {', '.join(f'`{o}`' for o in L['tokens'][t]['dynamic_code_owners'])}")
    w("")

    w("## Tokens with no consumer\n")
    w(f"_{m['orphan_count']} of {m['semantic_token_count']} semantic color tokens "
      "are referenced by no component token and no component code._\n")
    by_family = defaultdict(list)
    for t in L["orphans"]:
        by_family[L["tokens"][t]["family"]].append(t)
    for fam, toks in sorted(by_family.items()):
        w(f"### `{fam}` ({len(toks)})\n")
        for t in toks:
            w(f"- `{t}`")
        w("")

    w("## Per-token ledger\n")
    w("| Semantic token | Family | Bindings | Roles | States | Components | Direct | Brand-varies (L/D) |")
    w("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for tok, v in sorted(L["tokens"].items()):
        varies = ("yes" if v["modes"]["light"]["varies_by_brand"] else "no") + "/" + \
                 ("yes" if v["modes"]["dark"]["varies_by_brand"] else "no")
        comps = ", ".join(f"`{c}`" for c in v["component_consumers"]) or "—"
        direct = ", ".join(f"`{o}`" for o in v["direct_code_owners"]) or "—"
        w(f"| `{tok}` | {v['family']} | {v['binding_count']} "
          f"| {', '.join(v['roles']) or '—'} | {', '.join(v['states']) or '—'} "
          f"| {comps} | {direct} | {varies} |")
    w("")

    w("## Per-component contract\n")
    for comp, bs in L["components"].items():
        w(f"### `{comp}` ({len(bs)})\n")
        w("| Component token | Role | State | Semantic token |")
        w("| --- | --- | --- | --- |")
        for b in bs:
            state = f"{b['status']}/{b['state']}" if b["status"] else b["state"]
            w(f"| `{b['component_token']}` | {b['role']} | {state} | `{b['semantic_token']}` |")
        w("")

    if m["component_files_without_color"]:
        w("## Component token files declaring no colour\n")
        w("_These components take their colour entirely from elsewhere — a "
          "parent component, a wrapped primitive, or direct `.tsx` usage._\n")
        for f in m["component_files_without_color"]:
            w(f"- `{f}`")
        w("")

    if m["unclassified_leaf_words"]:
        w("## Unclassified leaf words\n")
        w("_Words in component-token leaf names the script could not map to a "
          "role, state, or status. Listed so the vocabulary can be refined "
          "rather than silently guessed at._\n")
        w("| Word | Occurrences |")
        w("| --- | --- |")
        for word, n in m["unclassified_leaf_words"].items():
            w(f"| `{word}` | {n} |")
        w("")

    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--code-repo", required=True, type=Path,
                    help="path to gsl-core-web-design-system")
    ap.add_argument("--include-inactive-brands", action="store_true",
                    help=f"include brands excluded by default ({', '.join(sorted(INACTIVE_BRANDS))})")
    ap.add_argument("--out", type=Path, default=Path(__file__).resolve().parent.parent / "color",
                    help="output directory")
    args = ap.parse_args()

    repo = args.code_repo.resolve()
    if not (repo / "libraries" / "tokens" / "src").exists():
        raise SystemExit(f"not a design-system repo: {repo}")

    ledger = build_ledger(repo, args.include_inactive_brands)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "color-usage-ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")
    (args.out / "color-usage-ledger.md").write_text(render_markdown(ledger))

    m = ledger["meta"]
    print(f"brands            : {', '.join(m['brands'])}"
          + (f"   (excluded: {', '.join(m['excluded_brands'])})" if m["excluded_brands"] else ""))
    print(f"semantic tokens   : {m['semantic_token_count']}")
    print(f"bindings          : {m['binding_count']} across {m['component_file_count']} component files")
    print(f"orphans           : {m['orphan_count']}")
    print(f"direct bypasses   : {m['direct_usage_count']}")
    print(f"dynamic-only      : {m['dynamic_only_count']}")
    print(f"role mismatches   : {m['role_family_mismatch_count']}")
    print(f"light collisions  : {m['light_mode_collision_count']}")
    print(f"unclassified words: {len(m['unclassified_leaf_words'])}")
    print(f"-> {args.out}/color-usage-ledger.json")
    print(f"-> {args.out}/color-usage-ledger.md")


if __name__ == "__main__":
    main()
