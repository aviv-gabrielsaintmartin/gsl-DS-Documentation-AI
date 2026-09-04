# Typography usage audit

_Human-facing audit only — this is **not** the AI-facing ruleset. It records what was actually observed on real screens, including the fact that no reliable per-size hierarchy rule could be found. An AI agent should not read this file as a semantic mapping to apply to new content — [typography-tokens.md](typography-tokens.md) is the file meant for that, and it deliberately stays short about this topic because there isn't yet a rule solid enough to state as one._

## Why this exists

The first pass at `typography-tokens.md` documented an inferred H1→H5 / Display-is-hero framing — plausible-looking, but never checked against a real screen. Auditing three live screens in Figma found no such ladder: a page's own title can render smaller than a section header further down the same page, and the same nominal role (a section/module label) gets different styles in different components. That finding is recorded here rather than folded into the tokens doc, so the tokens doc doesn't carry a theory an AI would read as more settled than it is.

## Method

- Sampled 3 real screens live via the Figma MCP, all in file `AI reference screen` (`bGX2uXc9TnTjpgZ1JUSPIk`):
  - Classified Detail Page — Buyer (Mobile) — `node-id=1-80293`
  - NLS Search FR - Result page (List) — `node-id=1-32219`
  - NLS Search FR - HP - Variant A (homepage) — `node-id=1-23002`
- For each, inspected the actual rendered text-node styles via `get_design_context` (not just token names) — code output shows the real bound font-size/line-height/weight per node, which is what surfaced the mismatch below.

## What was found

Size is chosen per block, driven by two things, not by page hierarchy:

1. **Local emphasis** — which element should visually dominate relative to its immediate neighbors inside the same block (e.g. a price outranking the title above it).
2. **Container size** — the same role gets a larger size when its block has more room (a full-width detail page) and a smaller one when the block is compact (a list card).

### Observed pairings

| Context | Element | Style |
| --- | --- | --- |
| Classified detail page (full width) | Price (primary) | `headline/28/bold` |
| Classified detail page | Price (secondary, struck-through) | `body/14/regular` |
| Classified detail page | Section header (Description / About the location / Finance) | `headline/22/bold` |
| Classified detail page | Property title | `body/16/bold` |
| Classified detail page | Key facts row, address, card copy | `body/14/regular` (separators/bold values in `body/14/bold`) |
| Search results list card | Price | `headline/24/bold` |
| Search results list card | Price/m² (secondary) | `body/14/regular` |
| Search results list card | Listing title | `body/16/bold` |
| Search results list card | Key facts, address | `body/14/regular` |
| Search results list card | Provider tag | `body/12/regular` |
| Homepage module ("Market trends") | Module title | `body/16/bold` |
| Homepage carousel ("Your last search") | Widget label | `body/14/bold` |
| Homepage carousel | Widget sub-label | `body/12/regular` |

`body/11`, `headline/20`, and `headline/32` were not observed as real rendered sizes on any of the three screens — no example pairing to give.

### Anomaly: token/render mismatch on the search results counter

The "1.124 Properties for sale" counter on the search results page has a text node whose bound style is tagged `headline/20/bold`, but the actual rendered spans are hand-overridden away from it: the count reads at 24px/32 line-height (matches `headline/24`) and the label reads at 16px/24 (matches `body/16`). The token nominally applied to the node doesn't describe what's actually on screen — a design-file authoring issue, not a typography-semantics finding. Worth a separate fix at the source; not something this token doc can resolve.

## Open questions / next steps

- **Display was never observed** on any of the 3 screens sampled, including the homepage. That weakens the original "hero-only" framing without disproving it — no dedicated marketing/landing screen has been sampled yet. Worth checking one before asserting Display is unused.
- **Does the local-emphasis + container-size mechanism generalize** beyond these 3 screens, or were these just the pages that happened to be consistent? More sampling would only ever add precedent, never produce a formula — decide how much precedent is enough before investing more time here.
- ~~**For existing coded components**, the real source of truth is likely the component's implementation, not Figma.~~ **Answered** — see the code-side pass below.
- **The counter token/render mismatch above** should probably be flagged to whoever owns that Figma file, independent of this review.

---

## Code-side pass — what the components actually bind

_Added after the original Figma pass. This answers that pass's own open question:
"for existing coded components, the real source of truth is likely the
component's implementation, not Figma." It is. Extracted mechanically by
[scripts/extract_typography_usage.py](../scripts/extract_typography_usage.py) from
`gsl-core-web-design-system`; full ledger in
[typography/typography-usage-ledger.md](typography-usage-ledger.md)._

### Only the font family varies by brand

All six live brands define the **same 32 styles** with byte-identical size,
weight, line height, letter spacing, case and decoration. `fontFamily` is the
only property that differs — and it differs in all 32:

| Brand | Font family |
| --- | --- |
| SL, SLN | `Cera SL sys` |
| LI, LIN | `Open Sans` |
| MA | `Poppins` |
| BD | `Gotham` |

`typography-tokens.md` previously opened "Text styles for all GSL products, set
in `Cera SL sys`" — true for two of six brands, with no brand section anywhere on
the page to signal otherwise. Corrected.

### 21 of 32 styles have no real component consumer

| | Count |
| --- | --- |
| Bound by at least one component | 11 |
| Bound only by `avatar`'s initials ramp | 6 |
| Bound by nothing | 15 |

**This does not make them dead** — and this audit's own Figma pass proves why.
`headline/28/bold` was observed as the classified-detail-page price, yet **no
component binds it**. Product pages set type directly, outside the component
library. The two passes agree; they are measuring different things.

What the code pass *can* say is narrower and still useful: **which styles you get
for free by using a component**, and which require setting type by hand.

### `avatar` uses the type scale as a sizing ramp

Ten bindings map an avatar pixel size to a text style, from `initials.24` →
`body/11/regular` up to `initials.128` → `display/45/regular`. That single
component is the only consumer of `body/11/regular`, `display/45/regular`, and
**every `regular` headline weight** (22, 24, 28, 32).

Consequence: in component terms, **Headline is bold-only**. Its regular weights
exist to size initials, not to express a heading.

### Display has no component consumer at all

Zero of the six Display styles is bound by any component for a semantic purpose
(`display/45/regular` appears only in the avatar ramp above).

Combined with the Figma pass — Display observed on none of three sampled screens
— that is two independent lines of evidence. The original open question
("genuinely unused, or just unsampled?") is now answered for components: unused.
It remains open for marketing/landing pages, which neither pass has sampled.

### Seven of eight underline styles are redundant

The system has two underline mechanisms, and only one was documented:

| Mechanism | Token | Consumer |
| --- | --- | --- |
| Full underlined style | `body/16/regular underlined` | `link.typography.standalone` |
| CSS decoration longhand | `typography.css.textDecoration.underline` | `link.typography.default` |

The longhand — defined in `shared/typographies.json`, `isLonghand: true` — adds
underline while inheriting size and weight. It covers the inline-link case at any
size, which is why the other seven `underlined` styles have no consumer.

**It was absent from the documentation entirely.** Now on
[typography-tokens.md](typography-tokens.md).

### What this changes

- `typography-tokens.md`: the `Cera SL sys` error fixed, a brand-theming section
  added, a `Used by` column on all 32 styles, the longhand token documented.
- The "no component consumer" caveat is stated on the page itself, so nobody
  reads the column as a deletion list.
- Rules for generation: [typography-rules-ai.md](typography-rules-ai.md).

### Still open

- **Display on a marketing/landing screen.** Neither pass has sampled one.
- **Whether the six avatar-only styles should stay in the scale**, or whether
  avatar should size initials some other way. A design question, not a code one.
