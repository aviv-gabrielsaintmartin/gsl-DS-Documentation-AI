<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2855502688/Breakpoint+tokens | Last modified: Aug 06, 2026 -->

# Breakpoint tokens

The seven viewport sizes the design system targets, and the frame dimensions that go with each.

`Breakpoint/Width` (and its alias `Min width`) has a confirmed code equivalent — code uses the same seven values as media-query thresholds. `Max width`, `Height`, and `Min height` are Design Spec references only.

One additional code-only tier, `base` (0–359px, no media query), sits below XS with no design tool equivalent — confirmed by dev as an intentional complement, not part of the seven-tier system below.

## Viewport ranges

| Size | Range |
| --- | --- |
| **XS** | 360 to 599 px |
| **SM** | 600 to 767 px |
| **MD** | 768 to 1023 px |
| **LG** | 1024 to 1279 px |
| **XL** | 1280 to 1535 px |
| **XXL** | 1536 to 1919 px |
| **XXXL** | 1920 px & more |

## Tokens (5)

| Token | XS | SM | MD | LG | XL | XXL | XXXL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Breakpoint/Width` | 360 | 600 | 768 | 1024 | 1280 | 1536 | 1920 |
| `Breakpoint/Min width` | 360 | 600 | 768 | 1024 | 1280 | 1536 | 1920 |
| `Breakpoint/Max width` | 599 | 767 | 1023 | 1279 | 1535 | 1919 | 7680 |
| `Breakpoint/Height` | 640 | 962 | 1024 | 768 | 720 | 864 | 1080 |
| `Breakpoint/Min height` | 640 | 962 | 1024 | 768 | 720 | 864 | 1080 |

`Breakpoint/Min width` and `Breakpoint/Min height` are aliases of `Breakpoint/Width` and `Breakpoint/Height`, so their values are always identical. They exist for auto-layout constraints, not as separate breakpoint data.
