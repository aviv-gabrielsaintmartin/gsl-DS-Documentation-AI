> **This page is evidence-based.** The **Used by** column lists the components
> that actually bind each token in `gsl-core-web-design-system`, generated from
> [color/color-usage-ledger.md](color-usage-ledger.md). **not used** means no
> component binds it — do not reach for it.
> Rules for generating UI: [color-rules-ai.md](color-rules-ai.md).
> Evidence and verdicts: [color-usage-audit.md](color-usage-audit.md).

## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for | Used by |
| --- | --- | --- | --- |
| `Border/base` | Standard strokes and outlines on components — the default starting point | Anything with a more specific match below | see below |
| `Border/Status` | Strokes on error, warning, success, or information states (validation, alerts) | General interactive borders (→ `Interactive`) | `checkbox`, `counterField`, `datePicker`, `dropdown` +5 |
| `Border/Active` | The stroke on a currently active/selected element (e.g. a focused input, selected chip) | Focus ring (→ `Focus`) | `tabs` |
| `Border/Focus` | **Nothing — not used on web.** Focus rings use the platform system colours (`Highlight`, `-webkit-focus-ring-color`) so they honour the user's OS settings. | Everything — never bind this | **not used** |
| `Border/Interactive` | Generic hover/pressed stroke on an interactive element with no other semantic role | Elements with a dedicated border family (Active, Focus, Status) | `buttonGroup`, `checkbox`, `chip`, `counterField` +8 · direct: `DateCalendar` |
| `Border/On-Primary / On-Secondary` | A stroke on an element that sits on top of a primary or secondary background | Strokes on default/light backgrounds | see below |
| `Border/Constant` | Fixed black or white stroke that must ignore brand and light/dark mode entirely | Anything that should re-theme | `badge`, `mapPin` (no component) |
| `Border/Transparent` | A **faint but real** edge — 10% opaque, for subtle structural separation. Not invisible. | Visible borders needing contrast; a truly invisible border | `avatar`, `button`, `floatingButtonGroup`, `slider` +1 · direct: `CoachMark` |

## Semantic usage

> **`Border/Transparent` is a faint edge, not an invisible one.** It is 10%
> opaque (`#3232321a`) — a subtle separation line, used by `button`'s floating
> variant and by `avatar`, `tooltip` and `floatingButtonGroup`.
>
> The system has **no fully-transparent border token**. `button` (20 bindings),
> `badge` (4) and `chip` (3) therefore bind `Surface/Transparent` (alpha `00`) or
> their own fill token to get a border that occupies space but renders
> invisibly — so filled and outlined variants share an outer size. That is a
> deliberate component-internal idiom, not a defect: see
> [color-usage-audit.md § A1–A3](color-usage-audit.md).


### Status

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Border/Status/Error` | Stroke on an input, card, or container in an error state — validation failure, failed action | Warning states (→ `Warning`) | `checkbox`, `counterField`, `datePicker`, `dropdown` +5 |
| `Border/Status/Information` | **Not used.** No component borders a control for information — only `Error` is interactive. | Any control border | **not used** |
| `Border/Status/Success` | **Not used.** No component borders a control for success — only `Error` is interactive. | Any control border | **not used** |
| `Border/Status/Warning` | **Not used.** No component borders a control for warning — only `Error` is interactive. | Any control border | **not used** |

### base

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Border/Default` | Standard stroke on a high-contrast outlined control — outlined button, badge. **Ships `Default` only: there is no `Hover` or `Pressed` leaf** — for those use `Interactive`. | Form controls (→ `Subdued`), structural containers (→ `Light`), disabled (→ `Disabled`), inverted backgrounds (→ `Default-Inverted`) | `badge`, `button`, `toggleButton` · direct: `Checkbox`, `unsafe` |
| `Border/Default-Inverted` | Standard stroke on a component sitting on a dark/inverted background | Standard-mode components (→ `Default`) | `badge`, `button`, `slider` |
| `Border/Subdued` | The standard stroke on a **form control** — input, checkbox, radio, toggle, select. The most-used border in the system. | Interactive borders needing contrast (→ `Interactive`) | `buttonGroup`, `checkbox`, `counterField`, `datePicker` +9 · direct: `SegmentedControl` |
| `Border/Light` | The stroke on a **structural container** — card, modal, accordion, top bar, divider. | Anything needing visible contrast | `accordion`, `buttonBar`, `card`, `divider` +3 · direct: `unsafe` |
| `Border/Surface` | A stroke that matches the surface level — nearly invisible separation between adjacent fills | Visible structural borders (→ `Default`, `Subdued`) | `datePicker` · direct: `unsafe` |
| `Border/Disabled` | Stroke on a disabled component | Interactive states (→ `Interactive`) | `badge`, `button`, `checkbox`, `counterField` +9 · direct: `DateCalendar` |
| `Border/Focus` | **Nothing — not used on web.** Every focusable component sets `outlineColor={['Highlight', '-webkit-focus-ring-color']}` instead, deliberately deferring to the platform. | Everything — never bind this | **not used** |
| `Border/Active` | **Legacy — `tabs` only.** The `Active` family is a fast-iteration artifact; the rest of the system expresses selected states with `Interactive/Default`. Do not use for new work. | Anything outside `tabs` (→ `Interactive/Default`) | `tabs` |
| `Border/Interactive` | Generic hover/pressed stroke with no other semantic role | Elements with a dedicated border family | `buttonGroup`, `checkbox`, `chip`, `counterField` +8 · direct: `DateCalendar` |
| `Border/On-Primary` | Stroke on an element sitting on a primary-coloured fill | Strokes on default backgrounds | `badge`, `button` |
| `Border/On-Secondary` | Stroke on an element sitting on a secondary-coloured fill | Strokes on default backgrounds | `badge`, `button` |
| `Border/Constant/Black` | Fixed black stroke, ignores brand and mode | Anything that should re-theme | `badge` |
| `Border/Constant/White` | Fixed white stroke, ignores brand and mode. **Its only consumer, `mapPin`, has no component in code** — treat as effectively unused. | Anything that should re-theme | `mapPin` (no component) |
| `Border/Accent/Light` | **Not used.** `Surface/Accent/Light` is used by four components; this border twin has no consumer. | Everything, until a real case appears | **not used** |
| `Border/Transparent` | A **faint but real** edge — 10% opaque. Separates a light floating surface from the page. Not invisible. | A truly invisible border (no token exists — see the note above); visible structural borders | `avatar`, `button`, `floatingButtonGroup`, `slider` +1 · direct: `CoachMark` |
| `Border/Transparent/Strong` | A slightly more visible transparent stroke — stronger ghost container edges | Solid borders needing colour contrast | `slider` |

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
