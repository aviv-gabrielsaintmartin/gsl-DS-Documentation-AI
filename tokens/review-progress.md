Tracks the category-by-category documentation review for `tokens/`. Read this before starting a review session, update it before ending one.

## What "review" means here

Values are already exported from Figma and trusted — no spot-check against Figma needed. A review checks:

1. The file follows the shared template: `Overview` (which family/layer — omit if there's only one), `Semantic usage` (when to use each specific token), `Tokens` (exact values).
2. `Semantic usage` is actually complete — every token has a "when to use" note, not just a bare value table.
3. Anything flagged as open/unconfirmed in the file itself is still accurate, or gets escalated here.

## Status

| Category | File | Status | Last reviewed | Notes |
| --- | --- | --- | --- | --- |
| Surface | `colors-tokens/surface.md` | Reviewed | 2026-09-03 | Full template. Two open flags in the file itself: `Accent/Light` vs `Active` resolve identically (unconfirmed), `Decorative` family still too vague. |
| Border | `colors-tokens/border.md` | Reviewed | 2026-09-03 | Full template. |
| Content | `colors-tokens/content.md` | Reviewed | 2026-09-03 | Full template. |
| Symbols | `colors-tokens/symbols.md` | Reviewed | 2026-09-03 | Full template. |
| Scale | `colors-tokens/scale.md` | Reviewed | 2026-09-03 | Full template. |
| Native | `colors-tokens/native.md` | Reviewed | 2026-09-03 | Single family, no Overview needed. |
| Background | `colors-tokens/background.md` | Reviewed | 2026-09-03 | Single family, no Overview needed. |
| Spacing | `spacing-tokens.md` | Reviewed | 2026-09-03 | Rebuilt this session — merged two prior files, added Overview + Semantic usage. |
| Typography | `typography-tokens.md` | Needs follow-up | 2026-09-03 | No Semantic usage layer at all — just three value tables (Display/Headline/Body), no "use this style for X" guidance. |
| Radius | `radius-tokens.md` | Not started | — | Only had mechanical cleanup (title dedup, rename) — no completeness review yet. |
| Shadow | `shadow-tokens.md` | Not started | — | Same. |
| Border width | `border-width-tokens.md` | Not started | — | Same. |
| Opacity | `opacity-tokens.md` | Not started | — | Same. |
| Z-Index | `z-index-tokens.md` | Not started | — | Already merges usage into the Tokens table via a "Use for" column — check if that's sufficient or needs a dedicated Semantic usage section. |
| Breakpoint | `breakpoint-tokens.md` | Not started | — | Same. |
| Grid | `grid-tokens.md` | Not started | — | Has an existing "unconfirmed" flag about no live grid layout system — re-check it's still accurate. |
| Motion | `motion-tokens.md` | Not started | — | Has an existing note that duration/easing pairing tokens don't exist yet — re-check it's still accurate. |

## Out of scope for now

- The `colors-tokens/surface-border-combination-audit.md` draft — left alone deliberately, not part of this review track.
- Figma value spot-checks — tokens are already exported and trusted; only revisit if something looks structurally wrong.
