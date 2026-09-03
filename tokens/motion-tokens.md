Duration and easing primitives for animations and transitions.

Implementation primitive — code runtime token

**These are primitives, not yet paired.** A ticket exists to define named semantic combinations (e.g. a "fast transition" pairing a specific duration with a specific easing curve) but it hasn't been actioned — do not assume any such combination tokens exist yet. Reference a duration and an easing directly until they do.

## Durations (7)

| Token | Value (ms) |
| --- | --- |
| `motionDuration.150` | 150 |
| `motionDuration.200` | 200 |
| `motionDuration.250` | 250 |
| `motionDuration.300` | 300 |
| `motionDuration.500` | 500 |
| `motionDuration.1000` | 1000 |
| `motionDuration.1500` | 1500 |

## Easings (4)

| Token | Value |
| --- | --- |
| `motionEasing.ease` | `cubic-bezier(0.25, 0.1, 0.25, 1.0)` |
| `motionEasing.ease-out` | `cubic-bezier(0, 0, 0.58, 1)` |
| `motionEasing.ease-in` | `cubic-bezier(0.42, 0, 1.0, 1.0)` |
| `motionEasing.linear` | `cubic-bezier(0, 0, 1, 1)` |

‌
