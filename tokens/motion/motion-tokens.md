Duration and easing primitives for animations and transitions. Code runtime
tokens.

> **This page is evidence-based.** Consumption checked against
> `gsl-core-web-design-system`.

**These are primitives, not yet paired.** A ticket exists to define named
semantic combinations (a "fast transition" pairing a duration with an easing) but
it has not been actioned — reference a duration and an easing directly until it
is.

## All four easings are in use, and they split by purpose

| Easing | Components | Used for |
| --- | --- | --- |
| `ease` | 14 | the default — state changes on controls: `button`, `checkbox`, `toggle`, `accordion`, `tabs`, `link` … |
| `ease-out` | 4 | things **arriving**: `dropdown`, `modal`, `snackbar` opening; `skeleton` shimmer |
| `ease-in` | 2 | things **leaving**: `modal`, `snackbar` closing |
| `linear` | 3 | continuous motion where acceleration would look wrong: `button` and `loadingState` spinners, `datePicker` |

`modal` and `snackbar` bind both `ease-out` and `ease-in` — the enter/exit pair.
That is the pattern to copy for anything that appears and dismisses.

## Durations (7)

| Token | ms | Components | Used by |
| --- | --- | --- | --- |
| `motionDuration.150` | 150 | 5 | `checkbox`, `datePicker`, `radio`, `textButton`, `toggle` |
| `motionDuration.200` | 200 | 8 | `button`, `buttonGroup`, `imageSlider`, `link`, `modal`, `snackbar`, `tabs`, `toggleButton` |
| `motionDuration.250` | 250 | 5 | `floatingButtonGroup`, `mediaUpload`, `modal`, `snackbar`, `tabs` |
| `motionDuration.300` | 300 | 5 | `accordion`, `carousel`, `dropdown`, `imageSlider`, `skeleton` |
| `motionDuration.500` | 500 | **0** | **no consumer** |
| `motionDuration.1000` | 1000 | 3 | `button`, `loadingState`, `mediaUpload` — looping/indeterminate |
| `motionDuration.1500` | 1500 | 1 | `skeleton` — the slowest loop |

Rough shape: **150–300 ms for interaction feedback, 1000–1500 ms for loops.**
`500` sits between the two and is used by nothing — the one gap in the scale.

## Easings (4)

| Token | Value | Components |
| --- | --- | --- |
| `motionEasing.ease` | `cubic-bezier(0.25, 0.1, 0.25, 1.0)` | 14 |
| `motionEasing.ease-out` | `cubic-bezier(0, 0, 0.58, 1)` | 4 |
| `motionEasing.linear` | `cubic-bezier(0, 0, 1, 1)` | 3 |
| `motionEasing.ease-in` | `cubic-bezier(0.42, 0, 1.0, 1.0)` | 2 |
