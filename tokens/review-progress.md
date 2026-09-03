Tracks the category-by-category documentation review for `tokens/`. Read this before starting a review session, update it before ending one.

## What "review" means here

Values are already exported from Figma and trusted — no spot-check against Figma needed. A review checks:

1. The file follows the shared template: `Overview` (which family/layer — omit if there's only one), `Semantic usage` (when to use each specific token), `Tokens` (exact values).
2. `Semantic usage` is actually complete — every token has a "when to use" note, not just a bare value table.
3. Anything flagged as open/unconfirmed in the file itself is still accurate, or gets escalated here.
4. If `Semantic usage` guidance can't be confirmed from the file or a naming convention alone, sample real screens live via Figma before writing it — don't infer a hierarchy or rule from convention and present it as settled.
5. If what comes out of that sampling is exploratory research rather than a confirmed rule, split it into a sibling `<category>-usage-audit.md` file — human-facing only, flagged not-AI-facing in its own header (see `typography-usage-audit.md` for the pattern, itself modelled on `colors-tokens/surface-border-combination-audit.md`) — so the main token doc stays short and AI-trustworthy.

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
| Typography | `typography-tokens.md` | Reviewed | 2026-09-03 | Rewritten after auditing 3 real screens in Figma (classified detail page, search results list, homepage) — no H1–H5 mapping exists in practice; size is a per-block choice (local emphasis + container size), not a lookup. Split the exploratory findings out into a new sibling file, `typography-usage-audit.md` (mirrors the existing `surface-border-combination-audit.md` pattern — human-facing only, not an AI-facing ruleset), so the main doc stays short and trustworthy. Open questions live there: Display unobserved on all 3 screens, a token/render mismatch found on one screen, and whether per-component code (not Figma) is the more reliable source of truth for existing components. |
| Radius | `radius-tokens.md` | Reviewed | 2026-09-03 | Added Semantic usage section (was intro + bare Tokens table only). Grounded `None` in Feedback message's doc. Then spot-checked live against 9 real Figma components (Card, Text Field, Snackbar, Text Button, Accordion, Coach mark, Button, Tag, Chip) since most components don't name a radius token in their own docs — confirmed the size/shape-tiered rule holds: `4`/`8`/`16` scale with card size (Card literally exposes `Radius=4/8/16` as a variant property), `8` also covers other mid-size rectangular containers/controls (Text Field, Snackbar, Text Button), `16` also covers larger containers (Accordion, Coach mark), and pill/`Radius/Rounded` covers filled interactive controls (Button, Tag, Chip) regardless of size — shape category matters as much as size (Text Button is small but rectangular, not pill). Pill components bind their own value (96–100) rather than literally `Radius/Rounded` (10000) — same visual result, confirmed non-issue per Gabriel. Noted but out of scope: Figma has an unimplemented "Corner radius" per-component semantic layer with no code equivalent. Page-level check done: spot-checked 3 real screens (bGX2uXc9TnTjpgZ1JUSPIk — home/search, search prompt, results list) — the size/shape-tiered rule holds everywhere checked (card `16`, badges/tags/buttons pill `100`, provider logo badge `8`/`4` nested), no wrong-tier values found. Radius is applied as a hardcoded pixel literal rather than a bound token/variable in every page node checked (unlike color/typography on the same nodes) — same known Figma-only "Corner radius" layer gap already noted, now confirmed to extend to real pages, not just the component library. Separately noticed (not a radius issue): the results-list "Newest ▾" sort control is a custom-built frame, not a real Button/Text Button instance, though its radius value is correct. |
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
