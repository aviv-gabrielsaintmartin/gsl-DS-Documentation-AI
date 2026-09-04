> **Design-authoring palette — not used in web code.**
> No component, icon, or illustration in `gsl-core-web-design-system` references
> a `Symbol/*` token. Icons paint via `fill: currentcolor` from a **Content**
> token; illustrations ship as pre-rendered `.webp` raster with their colours
> baked in at export. These tokens are applied in Figma when authoring an asset,
> never at runtime. An AI agent must never emit one — see
> [color-rules-ai.md](color-rules-ai.md) and
> [color-usage-audit.md § C2](color-usage-audit.md).

## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for |
| --- | --- | --- |
| `Symbol/Brand` | SVG and icon fills that carry brand identity — the primary colour of an icon or illustration element | Text fills (→ Content family); component fills (→ Surface family) |
| `Symbol/Disabled` | Icon or illustration fills in a disabled state — a scale from light to dark | Disabled text (→ `Content/Disabled`); disabled component backgrounds (→ `Surface/Disabled`) |
| `Symbol/Skin tones` | Human skin tone fills in illustrations and avatars only | Any product UI fill — these are illustration-only |

## Semantic usage

### Brand

| Token | When to use | Don't use for |
| --- | --- | --- |
| `Symbol/Brand/Primary/Default` | The main brand colour fill for an icon or SVG element — the dominant brand hue | Subdued/secondary icon fills (→ `Primary/Subdued`) |
| `Symbol/Brand/Primary/Subdued` | A lighter, tinted version of the brand fill — secondary icon element, decorative accent within an illustration | Primary icon fill (→ `Primary/Default`) |
| `Symbol/Brand/Secondary/Default` | A neutral secondary icon fill associated with the brand — used alongside Primary for two-tone icons | Primary brand fills (→ `Primary/Default`) |
| `Symbol/Brand/Dark` | A dark (near-black) icon fill — for icons needing contrast on light backgrounds without brand tinting | Brand-coloured fills (→ `Primary`) |
| `Symbol/Brand/Light` | A light icon fill — for icons on dark backgrounds needing contrast without brand tinting | Brand-coloured fills (→ `Primary`) |

### Disabled

*A greyscale scale (100 = lightest, 500 = darkest) for layered disabled icon/illustration fills. Pick the weight that gives sufficient contrast against the disabled background.*

| Token | When to use |
| --- | --- |
| `Symbol/Disabled/100` | Lightest disabled fill — icon on a white or near-white disabled background |
| `Symbol/Disabled/200` | Light disabled fill — icon on a light grey disabled background |
| `Symbol/Disabled/300` | Mid-light disabled fill |
| `Symbol/Disabled/400` | Mid-dark disabled fill |
| `Symbol/Disabled/500` | Darkest disabled fill — icon on a white background needing stronger contrast in disabled state |

### Skin tones

*Illustrations and avatars only — not for product UI fills. Numbers indicate relative lightness (100 = lightest, 1200 = darkest).*

| Token | When to use |
| --- | --- |
| `Symbol/SkinColors/Skin100–1200` | Human skin tone in an illustration or avatar. Match to the illustration's intended representation — do not pick based on visual preference alone. |

## Tokens

### Symbol — Brand (5)

*SVG and icon fills using brand identity colours.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Symbol/Brand/Dark` | `#000000` | `#525A76` | |
| `Color/Symbol/Brand/Light` | `#FFFFFF` | `#FCE6E7` | Brand-variant (Dark only) — see below |
| `Color/Symbol/Brand/Primary/Default` | `#E30513` | `#C10410` | Brand-variant — see below |
| `Color/Symbol/Brand/Primary/Subdued` | `#F8C3C6` | `#F8C3C6` | Brand-variant — see below |
| `Color/Symbol/Brand/Secondary/Default` | `#EEEEEE` | `#525A76` | Brand-variant — see below |

<details>
<summary>Brand variance — 4 of 5 tokens vary across the six brands (values below)</summary>

**Light**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Symbol/Brand/Primary/Default` | `#E30513` | `#CA2E5F` | `#017CBC` | `#FF9900` | `#BA903B` | `#003DF5` |
| `Symbol/Brand/Primary/Subdued` | `#F8C3C6` | `#FFC2CD` | `#C2E0EF` | `#FFEABC` | `#EEE4D0` | `#C4D4F7` |
| `Symbol/Brand/Secondary/Default` | `#EEEEEE` | `#EEEEEE` | `#EEEEEE` | `#FFFFFF` | `#EEEEEE` | `#EEEEEE` |

*Note: `Symbol/Brand/Light` does not vary in Light mode (constant `#FFFFFF`) — only its Dark value varies, shown below.*

**Dark**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Symbol/Brand/Light` | `#FCE6E7` | `#FCE6E7` | `#E6F2F8` | `#FFFFFF` | `#E0E0E0` | `#C4D4F7` |
| `Symbol/Brand/Primary/Default` | `#C10410` | `#890031` | `#017CBC` | `#FF9900` | `#84662A` | `#002BAE` |
| `Symbol/Brand/Primary/Subdued` | `#F8C3C6` | `#FFC2CD` | `#C2E0EF` | `#FFEABC` | `#D4B984` | `#C2D0FD` |
| `Symbol/Brand/Secondary/Default` | `#525A76` | `#525A76` | `#525A76` | `#525A76` | `#525A76` | `#000000` |

</details>

### Symbol — Disabled (5)

*Disabled-state icon and illustration fills.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Symbol/Disabled/100` | `#FFFFFF` | `#C9CDDB` | Brand-variant (Dark only) — see below |
| `Color/Symbol/Disabled/200` | `#EEEEEE` | `#AFB5C8` | |
| `Color/Symbol/Disabled/300` | `#E0E0E0` | `#979EB5` | |
| `Color/Symbol/Disabled/400` | `#AEAEAE` | `#7F87A0` | |
| `Color/Symbol/Disabled/500` | `#000000` | `#525A76` | |

<details>
<summary>Brand variance — Disabled/100 varies in Dark mode only (values below)</summary>

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Symbol/Disabled/100 (Dark)` | `#C9CDDB` | `#D0D1E6` | `#C9CDDB` | `#C9CDDB` | `#C9CDDB` | `#C9CDDB` |

</details>

### Symbol — Skin tones (12)

*Illustrations and avatars only.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Symbol/SkinColors/Skin100` | `#FCDCD2` | `#FCDCD2` | |
| `Color/Symbol/SkinColors/Skin200` | `#F5C09D` | `#F5C09D` | |
| `Color/Symbol/SkinColors/Skin300` | `#F0AA8F` | `#F0AA8F` | |
| `Color/Symbol/SkinColors/Skin400` | `#F9DCB1` | `#F9DCB1` | |
| `Color/Symbol/SkinColors/Skin500` | `#FED1A5` | `#FED1A5` | |
| `Color/Symbol/SkinColors/Skin600` | `#FAAD73` | `#FAAD73` | |
| `Color/Symbol/SkinColors/Skin700` | `#CC8E4A` | `#CC8E4A` | |
| `Color/Symbol/SkinColors/Skin800` | `#CD7D37` | `#CD7D37` | |
| `Color/Symbol/SkinColors/Skin900` | `#B25D20` | `#B25D20` | |
| `Color/Symbol/SkinColors/Skin1000` | `#864C2C` | `#864C2C` | |
| `Color/Symbol/SkinColors/Skin1100` | `#864C2C` | `#563117` | |
| `Color/Symbol/SkinColors/Skin1200` | `#563117` | `#51331D` | |
