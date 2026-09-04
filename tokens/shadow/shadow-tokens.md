> **This page is evidence-based.** Consumption checked against `gsl-core-web-design-system`. Reasoning: [shadow-usage-audit.md](shadow-usage-audit.md).

Elevation shadows, named by blur radius. All are drop shadows with no spread and no horizontal offset, at a fixed colour of `#00000029` (black, 16% opacity). Defined as composite elevation styles.

## Semantic usage

| Tier | When to use |
| --- | --- |
| `none` | Inline/flat content with no elevation: the non-floating Feedback message variant, a full-screen Modal (nothing behind it to separate from), and buttons in their default on-page style. |
| `4` | Minimal-elevation floating elements anchored tightly to a trigger or another surface: Floating button group, Selectable list, Slider handle, Coachmark. |
| `8` | Used by: Action Menu, Button's floating variant, Date picker, Top bar, and the floating Feedback message variant. |
| `16` | Used by: Snackbar, Tooltip, mobile Bottom Sheet. |
| `24`, `32` | **No consumer.** Confirmed from code, not just unsampled: no component token and no component binds either. The elevation scale components actually use tops out at `16`. |

> **Corrected against code.** The Figma pass recorded Action Menu's dropdown at
> tier `4`; `actionMenu.json` binds **`shadow.8`**. The component lists above are
> now taken from the code bindings. Worth a Figma check — one of the two is
> wrong, and code is the one that ships.

**Open question:** no confirmed rule distinguishes `8` from `16` — both are used by similarly-sized floating notification-style components (the floating Feedback message vs. Snackbar). Treat each as "this is what the named component currently uses," not a generalizable rule for new components. See [shadow-usage-audit.md](shadow-usage-audit.md) for the reasoning and what was ruled out.

**Note:** several components render their shadow via CSS `filter: drop-shadow(...)` rather than `box-shadow`. When rendered that way, the blur radius shown is exactly half the token's value (e.g. tier `16`'s `radius 16` renders as `8px` blur) — offset stays the same. This is a rendering-technique artifact of `drop-shadow`'s blur math, confirmed consistent across every `drop-shadow`-rendered instance checked; it is not a token drift and needs no fix.

## Tokens

| Style | Blur radius | Y offset | Components | Used by |
| --- | --- | --- | --- | --- |
| `none` | — | — | 2 | `modal`, `selectableList` |
| `4` | 4 | 1 | 3 | `floatingButtonGroup`, `selectableList`, `slider` · direct: `CoachMark` |
| `8` | 8 | 2 | 4 | `actionMenu`, `button`, `datePicker`, `topBar` · direct: `FeedbackMessage` |
| `16` | 16 | 4 | 3 | `modal`, `snackbar`, `tooltip` |
| `24` | 24 | 6 | **0** | **no component** |
| `32` | 32 | 8 | **0** | **no component** |

`none` is an explicit code reset value — design specs express no shadow by absence of an effect
