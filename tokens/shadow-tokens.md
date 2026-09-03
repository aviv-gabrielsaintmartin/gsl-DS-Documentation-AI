Elevation shadows, named by blur radius. All are drop shadows with no spread and no horizontal offset, at a fixed colour of `#00000029` (black, 16% opacity). Defined as composite elevation styles.

## Semantic usage

| Tier | When to use |
| --- | --- |
| `none` | Inline/flat content with no elevation: the non-floating Feedback message variant, a full-screen Modal (nothing behind it to separate from), and buttons in their default on-page style. |
| `4` | Minimal-elevation floating elements anchored tightly to a trigger or another surface: Action Menu's dropdown list, Coachmark, Slider handle. |
| `8` | Used by: floating action button (Button's `Style=Floating (On-content)` variant), the floating Feedback message variant. |
| `16` | Used by: Snackbar, Tooltip, mobile Bottom Sheet. |
| `24`, `32` | Not observed in any sampled component — unconfirmed, flagging rather than guessing. |

**Open question:** no confirmed rule distinguishes `8` from `16` — both are used by similarly-sized floating notification-style components (the floating Feedback message vs. Snackbar). Treat each as "this is what the named component currently uses," not a generalizable rule for new components. See [shadow-usage-audit.md](shadow-usage-audit.md) for the reasoning and what was ruled out.

**Note:** several components render their shadow via CSS `filter: drop-shadow(...)` rather than `box-shadow`. When rendered that way, the blur radius shown is exactly half the token's value (e.g. tier `16`'s `radius 16` renders as `8px` blur) — offset stays the same. This is a rendering-technique artifact of `drop-shadow`'s blur math, confirmed consistent across every `drop-shadow`-rendered instance checked; it is not a token drift and needs no fix.

## Tokens

| Style | Blur radius | Y offset |
| --- | --- | --- |
| `none` | — | — |
| `4` | 4 | 1 |
| `8` | 8 | 2 |
| `16` | 16 | 4 |
| `24` | 24 | 6 |
| `32` | 32 | 8 |

`none` is an explicit code reset value — design specs express no shadow by absence of an effect
