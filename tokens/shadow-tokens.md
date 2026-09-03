Elevation shadows, named by blur radius. All are drop shadows with no spread and no horizontal offset, at a fixed colour of `#00000029` (black, 16% opacity). Defined as composite elevation styles.

## Semantic usage

Confirmed live against 8 real Figma components (Action Menu, Coachmark, Feedback message, Snackbar, Slider, Tooltip, Modal, Bottom Sheet) — a component set node (`Button`) failed to load twice and wasn't checked directly, but its "floating" variant is visible inside Action Menu.

| Tier | When to use |
| --- | --- |
| `none` | Inline/flat content with no elevation: the non-floating Feedback message variant, a full-screen Modal (nothing behind it to separate from), and buttons in their default on-page style. |
| `4` | Minimal-elevation floating elements anchored tightly to a trigger or another surface: Action Menu's dropdown list, Coachmark, Slider handle. |
| `8` | Used by: floating action button (Button's `Style=Floating (On-content)` variant), the floating Feedback message variant. |
| `16` | Used by: Snackbar, Tooltip, mobile Bottom Sheet. |
| `24`, `32` | Not observed in any sampled component — unconfirmed, flagging rather than guessing. |

**Open question — `8` vs `16`:** no confirmed rule distinguishes these two tiers. The floating Feedback message (`8`) and Snackbar (`16`) are both floating, temporary, similarly-sized notification-style components — nothing found in the components themselves (size, anchoring, persistence) explains why one gets less elevation than the other. A stacking-order rationale (e.g. Snackbar rendering visually above a Feedback message) is plausible but unverified — no screen was found showing both together, and no z-index documentation confirms a stacking order between them. Treat `8` vs `16` as "this is what each named component currently uses," not as a generalizable rule for new components.

**Implementation note:** several components render their shadow via CSS `filter: drop-shadow(...)` rather than `box-shadow`. When rendered that way, the blur radius shown is exactly half the token's value (e.g. tier `16`'s `radius 16` renders as `8px` blur) — offset stays the same. This is a rendering-technique artifact of `drop-shadow`'s blur math, confirmed consistent across every `drop-shadow`-rendered instance checked; it is not a token drift and needs no fix.

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
