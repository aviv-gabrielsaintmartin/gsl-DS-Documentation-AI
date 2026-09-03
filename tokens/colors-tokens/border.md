## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for |
| --- | --- | --- |
| `Border/base` | Standard strokes and outlines on components — the default starting point | Anything with a more specific match below |
| `Border/Status` | Strokes on error, warning, success, or information states (validation, alerts) | General interactive borders (→ `Interactive`) |
| `Border/Active` | The stroke on a currently active/selected element (e.g. a focused input, selected chip) | Focus ring (→ `Focus`) |
| `Border/Focus` | Keyboard focus ring only — accessibility indicator | Active/selected states (→ `Active`) |
| `Border/Interactive` | Generic hover/pressed stroke on an interactive element with no other semantic role | Elements with a dedicated border family (Active, Focus, Status) |
| `Border/On-Primary / On-Secondary` | A stroke on an element that sits on top of a primary or secondary background | Strokes on default/light backgrounds |
| `Border/Constant` | Fixed black or white stroke that must ignore brand and light/dark mode entirely | Anything that should re-theme |
| `Border/Transparent` | A near-invisible stroke for subtle structural separation without a hard line | Visible borders needing colour contrast |

## Semantic usage

### Status

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Border/Status/Error` | Stroke on an input, card, or container in an error state — validation failure, failed action | Warning states (→ `Warning`) |
| `Border/Status/Information` | Stroke on an informational container — tips, announcements | Actionable/urgent states (→ `Warning`, `Error`) |
| `Border/Status/Success` | Stroke on a container confirming a completed action | Ongoing/neutral info (→ `Information`) |
| `Border/Status/Warning` | Stroke on a container flagging something the user should review | Confirmed failures (→ `Error`) |

### base

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Border/Default` | Standard stroke on a component in its default state | Disabled (→ `Disabled`), inverted backgrounds (→ `Default-Inverted`) |
| `Border/Default-Inverted` | Standard stroke on a component sitting on a dark/inverted background | Standard-mode components (→ `Default`) |
| `Border/Subdued` | A muted, lower-contrast stroke — dividers, secondary separators | Interactive borders needing contrast (→ `Interactive`) |
| `Border/Light` | The lightest structural stroke — very subtle container edges | Anything needing visible contrast |
| `Border/Surface` | A stroke that matches the surface level — nearly invisible separation between adjacent fills | Visible structural borders (→ `Default`, `Subdued`) |
| `Border/Disabled` | Stroke on a disabled component | Interactive states (→ `Interactive`) |
| `Border/Focus` | Keyboard focus ring — accessibility indicator only | Active/selected states (→ `Active`) |
| `Border/Active` | Stroke on an active/selected element (e.g. selected chip, focused text field) | Keyboard focus ring (→ `Focus`) |
| `Border/Interactive` | Generic hover/pressed stroke with no other semantic role | Elements with a dedicated border family |
| `Border/On-Primary` | Stroke on an element sitting on a primary-coloured fill | Strokes on default backgrounds |
| `Border/On-Secondary` | Stroke on an element sitting on a secondary-coloured fill | Strokes on default backgrounds |
| `Border/Constant/Black` | Fixed black stroke, ignores brand and mode | Anything that should re-theme |
| `Border/Constant/White` | Fixed white stroke, ignores brand and mode | Anything that should re-theme |
| `Border/Accent/Light` | A light, brand-tinted accent stroke — mirrors `Surface/Accent/Light` use cases | Status borders (→ Status family) |
| `Border/Transparent` | A near-invisible stroke for very subtle separation — ghost containers, barely-there dividers | Visible structural borders |
| `Border/Transparent/Strong` | A slightly more visible transparent stroke — stronger ghost container edges | Solid borders needing colour contrast |

## Tokens

### Status (6)

*Status-state strokes.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Border/Status/Error/Default` | `#B32730` | `#E89597` | |
| `Color/Border/Status/Error/Hover` | `#881E24` | `#EFB9BB` | |
| `Color/Border/Status/Error/Pressed` | `#5E1519` | `#F6DCDD` | |
| `Color/Border/Status/Information/Default` | `#006591` | `#8DAFCE` | |
| `Color/Border/Status/Success/Default` | `#006D31` | `#8DB596` | |
| `Color/Border/Status/Warning/Default` | `#7F561C` | `#E69B33` | |

### base (21)

*Strokes and outlines.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Border/Accent/Light/Default` | `#FCE6E7` | `#2E0000` | Brand-variant — see below |
| `Color/Border/Active/Default` | `#E30513` | `#BD0F1A` | Brand-variant — see below |
| `Color/Border/Active/Pressed` | `#C10410` | `#C6303A` | Brand-variant — see below |
| `Color/Border/Constant/Black` | `#000000` | `#15171E` | |
| `Color/Border/Constant/White` | `#FFFFFF` | `#F8F8FA` | |
| `Color/Border/Default-Inverted/Default` | `#FFFFFF` | `#292D3B` | |
| `Color/Border/Default/Default` | `#323232` | `#E3E5ED` | |
| `Color/Border/Disabled` | `#E0E0E0` | `#525A76` | |
| `Color/Border/Focus` | `#C10410` | `#F8C3C6` | Brand-variant — see below |
| `Color/Border/Interactive/Default` | `#4B4B4B` | `#C9CDDB` | |
| `Color/Border/Interactive/Hover` | `#323232` | `#E3E5ED` | |
| `Color/Border/Interactive/Pressed` | `#000000` | `#F8F8FA` | |
| `Color/Border/Light/Default` | `#E0E0E0` | `#525A76` | |
| `Color/Border/On-Primary/Default` | `#FFFFFF` | `#F8F8FA` | Brand-variant — see below |
| `Color/Border/On-Primary/Disabled` | `#FFFFFF99` | `#F8F8FA99` | Brand-variant — see below |
| `Color/Border/On-Secondary/Default` | `#323232` | `#F8F8FA` | |
| `Color/Border/On-Secondary/Disabled` | `#32323299` | `#F8F8FA99` | |
| `Color/Border/Subdued/Default` | `#959595` | `#7F87A0` | |
| `Color/Border/Surface/Default` | `#EEEEEE` | `#525A76` | |
| `Color/Border/Transparent/Default` | `#3232321a` | `#F8F8FA1a` | |
| `Color/Border/Transparent/Strong/Default` | `#32323233` | `#F8F8FA33` | |

<details>
<summary>Brand variance — 6 of 21 tokens vary across the six brands (values below)</summary>

**Light**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Border/Accent/Light/Default` | `#FCE6E7` | `#FFECEF` | `#E6F2F8` | `#FFF9EB` | `#F8F4EB` | `#C4D4F7` |
| `Border/Active/Default` | `#E30513` | `#CA2E5F` | `#017CBC` | `#FF9900` | `#BA903B` | `#003DF5` |
| `Border/Active/Pressed` | `#C10410` | `#AD0047` | `#006AA1` | `#CF6D00` | `#9E7A32` | `#0034D0` |
| `Border/Focus` | `#C10410` | `#AD0047` | `#017CBC` | `#CF6D00` | `#9E7A32` | `#2E60F7` |
| `Border/On-Primary/Default` | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#323232` | `#FFFFFF` | `#FFFFFF` |
| `Border/On-Primary/Disabled` | `#FFFFFF99` | `#FFFFFF99` | `#FFFFFF99` | `#32323299` | `#FFFFFF99` | `#FFFFFF99` |

**Dark**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Border/Accent/Light/Default` | `#2E0000` | `#42000F` | `#005986` | `#400D00` | `#54411B` | `#00238C` |
| `Border/Active/Default` | `#BD0F1A` | `#DC4B72` | `#2E94C9` | `#FFB02F` | `#C6A45E` | `#2E60F7` |
| `Border/Active/Pressed` | `#C6303A` | `#F0738F` | `#5EADD5` | `#FFC55E` | `#D4B984` | `#5E85F9` |
| `Border/Focus` | `#F8C3C6` | `#F0738F` | `#5EADD5` | `#FFB02F` | `#D4B984` | `#91ACFB` |
| `Border/On-Primary/Default` | `#F8F8FA` | `#F8F8FA` | `#F8F8FA` | `#15171E` | `#F8F8FA` | `#F8F8FA` |
| `Border/On-Primary/Disabled` | `#F8F8FA99` | `#F8F8FA99` | `#F8F8FA99` | `#15171E99` | `#F8F8FA99` | `#F8F8FA99` |

</details>
