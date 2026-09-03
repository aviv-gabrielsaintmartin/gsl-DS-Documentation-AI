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
- **For existing coded components**, the real source of truth for "which token does this component use" is likely the component's implementation, not Figma — a component's title slot may already hardcode a token choice, removing the ambiguity this audit describes for that case entirely. That's a per-component code question (in scope for the `component-web-ai-docs` skill against the real component library), not something to resolve in this token doc.
- **The counter token/render mismatch above** should probably be flagged to whoever owns that Figma file, independent of this review.
