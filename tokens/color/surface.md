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
| `Surface/base` | The default starting point for most components — cards, sheets, standard containers | Anything with a more specific match below | see below |
| `Surface/Brand` | CTAs and primary/secondary brand-identity fills | Non-branded interactive elements (→ `Interactive`) | `badge`, `button`, `card`, `progressBar` +2 |
| `Surface/Status` | Feedback messages, inline alerts, validation states (error/warning/success/info) | Persistent quality tiers (→ `Score`) | `button`, `checkbox`, `feedbackMessage`, `mediaUpload` +6 |
| `Surface/Score` | Advertiser/listing quality tier badges (Diamond–Bronze) | Status/feedback states (→ `Status`) | **not used** |
| `Surface/Interactive & Active` | Generic hover/pressed/selected/active states with no other semantic role | Elements with a dedicated family already (Status, Brand, Score) | see below |
| `Surface/Constant` | Fixed black/white fills that must ignore brand and light/dark mode entirely | Anything that should re-theme (→ `base`, `Default/Inverted`) | `badge`, `button`, `imageSlider`, `mediaUpload` +1 |
| `Surface/Transparent` | See-through washes with no solid colour, for subtle interaction feedback | Visible/solid state changes (→ `Interactive`) | `actionMenu`, `badge`, `button`, `cellContent` +12 · direct: `Chip`, `DateCalendar` |
| `Surface/On-Brand / On-Primary / On-Secondary` | An element's own fill when it sits on top of a brand/primary/secondary surface | The brand/primary/secondary surface itself | see below |
| `Surface/Data visualisation` | Charts and graphs only | Product UI, ever — even if a colour looks right | see below |
| `Surface/Decorative` | **One documented exception only** (the `rating` star). Brand- and mode-invariant accent with no state meaning and no general usage rule — see the Decorative section. | New work of any kind (→ use `<Rating>`, or raise the need for `Content/Decorative/*`) | `rating` |

## Semantic usage

> **Pick the sub-family by what the element *is*.** The three hover/pressed
> sub-families are not interchangeable — each has a consistent meaning in real
> usage:
>
> | The element is… | Default | Hover | Pressed |
> | --- | --- | --- | --- |
> | A **container or row** that reacts to pointer | `Default/Default` | `Default/Hover` | `Default/Pressed` |
> | An **interactive control** with a fill | `Default/Default` | `Interactive/Hover` | `Interactive/Pressed` |
> | A **ghost control** — no fill, still needs feedback | `Transparent/Default` | `Transparent/Hover` | `Transparent/Pressed` |
>
> Container: `accordion`, `cellContent`, `topBar`, `tabs`. Control: `chip`,
> `actionMenu`, `buttonGroup`, `selectableList`, `slider`. Ghost: `button`
> (tertiary), `pagination`, `toggleButton`.
>
> **A fill is always a `Surface/*` token, and a `Surface/*` token is always a
> fill.** Never bind a border or an icon to one — `button`, `badge` and `chip`
> currently do, and those are recorded defects. (`rating` also does, but as a
> documented exception — see `Decorative` below.)


### Brand

| Token | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Brand/Primary` | Main brand-coloured CTA fill — primary buttons, key actions, one per screen/section | Secondary or supporting fills (→ `Surface/Brand/Secondary`) | `badge`, `button`, `card`, `progressBar` +2 |
| `Surface/Brand/Secondary` | **Not used.** Only `Brand/Primary` has consumers. | Everything, until a real case appears | **not used** |

### Status

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Status/Error` | Light error background — feedback message body, inline validation banner | Solid/high-contrast error fills (→ `Error-Strong`) | `feedbackMessage`, `mediaUpload`, `selectCardGroup`, `statusTag` +1 |
| `Surface/Status/Error-Strong` | Solid, high-contrast error fill — error badges, icon containers, anything needing strong emphasis | Banner/message backgrounds (→ `Error`) | `button`, `checkbox`, `radio`, `tag` |
| `Surface/Status/Information` | Light informational background — tips, neutral announcements | Solid info fills (→ `Information-Strong`) | `feedbackMessage`, `statusTag`, `tag` |
| `Surface/Status/Information-Strong` | Solid, high-contrast info fill | Banner/message backgrounds (→ `Information`) | `tag` |
| `Surface/Status/Success` | Light success background — confirmation banners | Solid success fills (→ `Success-Strong`) | `feedbackMessage`, `statusTag`, `tag` |
| `Surface/Status/Success-Strong` | Solid, high-contrast success fill | Banner/message backgrounds (→ `Success`) | `progressBar`, `progressCircle`, `tag` |
| `Surface/Status/Warning` | Light warning background | Solid warning fills (→ `Warning-Strong`) | `feedbackMessage`, `statusTag`, `tag` |
| `Surface/Status/Warning-Strong` | Solid, high-contrast warning fill | Banner/message backgrounds (→ `Warning`) | `tag` |

*General rule across all four: `-Strong` is a contrast/weight choice (solid fill vs. light wash), not a severity escalation — don't reach for `-Strong` just because a message feels more urgent.*

### Score

| Token | When to use | Used by |
| --- | --- | --- |
| `Surface/Score/Diamond` | Highest advertiser/listing quality tier | **not used** |
| `Surface/Score/Gold` | Second-highest tier | **not used** |
| `Surface/Score/Silver` | Third tier | **not used** |
| `Surface/Score/Bronze` | Lowest tier | **not used** |

*Score tag backgrounds only. Never substitute for `Surface/Status/*` — Score is a tier ranking, not a state.*

### Data visualisation

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Data/Categorical` | Distinct, unordered categories in a chart (up to 5 series) | Ordered/magnitude data (→ Sequential) | dynamic |
| `Surface/Data/Categorical/Disabled` | A categorical series that's toggled off/inactive in a legend | Any in-use series | dynamic |
| `Surface/Data/Sequential` | Data with a single ordered magnitude, low to high (e.g. a heatmap of one metric) | Data with a meaningful zero-crossing (→ Diverging) | dynamic |
| `Surface/Data/Diverging` | Data with a meaningful midpoint — deviation above/below a baseline (e.g. profit/loss) | Simple ordered magnitude (→ Sequential) | dynamic |

*Charts and graphs only — never product UI, regardless of how well a colour happens to fit.*

### Constant

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Constant/Black` | Fixed black fill and its interaction states, ignoring brand and light/dark mode | Anything that should re-theme (→ `Surface/Default/Inverted`) | `imageSlider`, `mediaUpload`, `tag` |
| `Surface/Constant/Black/Transparent/Strong` | Strong black scrim/overlay, fixed opacity regardless of mode | Subtle overlays (→ `Transparent/Subdued`) | `mediaUpload` |
| `Surface/Constant/Black/Transparent/Subdued` | **Not used.** `Transparent/Strong` is the only scrim with consumers (`mediaUpload`). | Scrims (→ `Transparent/Strong`) | **not used** |
| `Surface/Constant/White` | Fixed white fill and its interaction states, ignoring brand and light/dark mode | Anything that should re-theme (→ `Surface/Default`) | `badge`, `button`, `tag` |

### Transparent

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Transparent` | A see-through fill over a light/default-mode background — subtle hover/press wash with no solid colour | Fills over dark/inverted content (→ `Transparent-Inverted`) | `actionMenu`, `badge`, `button`, `cellContent` +12 · direct: `Chip`, `DateCalendar` |
| `Surface/Transparent-Inverted` | A see-through fill over a dark/inverted background | Fills over standard-mode content (→ `Transparent`) | `button`, `progressBar`, `progressCircle` |

### On-Brand / On-Primary / On-Secondary

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/On-Brand` | An element's interaction-state fill when it sits directly on a brand-coloured surface | Elements on the default page background | `button` |
| `Surface/On-Primary/Transparent` | A transparent interaction wash for an element on a primary-coloured fill (e.g. hover on an icon inside a primary button) | Solid on-primary fills — this family is transparency-only | `button` |
| `Surface/On-Secondary/Transparent` | Same, on a secondary-coloured fill | Solid on-secondary fills | `button` · direct: `unsafe` |

### Interactive & Active

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Accent/Light` | A light, brand-tinted accent fill for highlighting content without implying selection | Selected/active state (→ `Active`) — see flag below | `card`, `progressBar`, `progressCircle`, `tag` |
| `Surface/Active` | **Legacy — `tabs` only.** `Active/Default` is unused; `Hover`/`Pressed` are bound by `tabs`, and `progressBar`/`progressCircle` borrow `Active/Pressed` as a static fill (a recorded defect). Do not use for new work. | Anything outside `tabs` (→ `Interactive/Selected`) | `progressBar`, `progressCircle`, `tabs` |
| `Surface/Interactive` | Generic hover/pressed fill for any interactive element with no other semantic role | Elements with a dedicated state family (Status, Active, Selected) | `actionMenu`, `buttonGroup`, `checkbox`, `chip` +10 · direct: `DateCalendar`, `SegmentedControl` |
| `Surface/Interactive/Selected` | The fill for an item in a persisted selected state (e.g. a chosen radio card, toggled filter) | Momentary active/highlight (→ `Active`) | `actionMenu`, `buttonGroup`, `checkbox`, `chip` +9 · direct: `DateCalendar`, `SegmentedControl` |

> **Resolved — use `Accent/Light`.** The two do resolve to the same hex in both
> modes and all six brands, but usage settles it: `Accent/Light/Default` has four
> consumers (`card`, `progressBar`, `progressCircle`, `tag`) while
> `Active/Default` has **none**. The `Active` family is a fast-iteration artifact
> whose only real consumer is `tabs` — see
> [color-usage-audit.md § B4](color-usage-audit.md). For a new tinted accent
> fill, use `Accent/Light`.

### Decorative

| Token | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Decorative/Red` | **Not used.** No consumer. | Everything, until a real case appears | **not used** |
| `Surface/Decorative/Yellow` | The `rating` star fill — a **documented exception**, brand- and mode-invariant by design. Not a precedent: reach for `<Rating>`, not this token. | Any new element (→ `<Rating>`, or raise the need for `Content/Decorative/*`) | `rating` |

*Decorative tokens carry brand/visual accent, not state. If an element's colour is meant to communicate something (error, active, tier), that's a missed semantic case, not a Decorative one.*

> **Still open — and the two tokens don't behave alike.** `Decorative/Yellow` is
> mode-invariant (`#FFB868` in light *and* dark, all six brands);
> `Decorative/Red` flips (`#DC3741` → `#E26C71`) and has no consumer. If
> `Decorative` means "a fixed accent that ignores the theme", Red contradicts it.
> The family has no settled definition, so no usage rule can be written for it.
>
> Its one live binding — `rating.color.starIcon` — is a **documented exception**,
> not a defect: no Content-family decorative token exists, and a rating star is
> amber by cross-product convention rather than by brand, so mode-invariance is
> correct. The structurally right home is `Content/Decorative/*`; that token
> should be created only once a second use case justifies it. See
> [color-usage-audit.md § A5](color-usage-audit.md).
>
> Until then: **do not use `Decorative` in new work.** Use `<Rating>` for a
> rating display.

### base

| Token root | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Surface/Default` | The default fill for most components — cards, sheets, standard containers. Start here. | Page-level canvas (→ `Background/Default`) | `accordion`, `actionMenu`, `avatar`, `button` +21 · direct: `CoachMark`, `DateCalendar` |
| `Surface/Default/Inverted` | A component fill that should flip against the page's light/dark mode (e.g. a dark card in light mode) | Fixed-colour needs regardless of mode (→ `Constant`) | `snackbar`, `tooltip` · direct: `CoachMark`, `unsafe` |
| `Surface/Light` | A lighter component fill for subtle recessed containers within a component | Page-level background (→ `Background/Light`) | `avatar`, `card`, `counterField`, `mediaUpload` +2 · direct: `SegmentedControl` |
| `Surface/Light/Transparent` | A translucent, very subtle wash — barely-visible hover/press feedback | Visible state changes (→ `Surface/Interactive`) | `wizard` |
| `Surface/Subdued` | A muted component fill — de-emphasised containers | Disabled state (→ `Surface/Disabled`) | `accordion`, `carousel`, `selectCardGroup`, `tag` · direct: `Chip` |
| `Surface/Disabled` | The fill for a disabled component | Muted-but-interactive containers (→ `Subdued`) | `accordion`, `badge`, `button`, `buttonGroup` +14 |
| `Surface/Dark` | **A neutral fill that must stay distinguishable from a white or light foreground.** Brand-invariant grey; white on it gives exactly 3.0:1, the WCAG non-text floor (`Surface/Subdued` would give 1.16:1 and fail). Use for an unselected control track, an active indicator dot, or a thumbnail scrim. | A general dark background (→ `Default/Inverted`) | `buttonGroup`, `carousel`, `mediaUpload`, `toggle` |

## Tokens

### Brand (4)

*CTAs, primary actions, brand accents.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Brand/Primary/Default` | `#E30513` | `#BD0F1A` | Brand-variant — see below |
| `Color/Surface/Brand/Primary/Hover` | `#C10410` | `#C6303A` | Brand-variant — see below |
| `Color/Surface/Brand/Primary/Pressed` | `#A1040D` | `#D05159` | Brand-variant — see below |
| `Color/Surface/Brand/Secondary/Default` | `#000000` | `#292D3B` | |

<details>
<summary>Brand variance — 3 of 4 tokens vary across the six brands (values below)</summary>

**Light**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Surface/Brand/Primary/Default` | `#E30513` | `#CA2E5F` | `#017CBC` | `#FF9900` | `#BA903B` | `#003DF5` |
| `Surface/Brand/Primary/Hover` | `#C10410` | `#AD0047` | `#006AA1` | `#CF6D00` | `#9E7A32` | `#0034D0` |
| `Surface/Brand/Primary/Pressed` | `#A1040D` | `#890031` | `#005986` | `#9F4600` | `#84662A` | `#002BAE` |

**Dark**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Surface/Brand/Primary/Default` | `#BD0F1A` | `#DC4B72` | `#2E94C9` | `#FFB02F` | `#C6A45E` | `#2E60F7` |
| `Surface/Brand/Primary/Hover` | `#C6303A` | `#F0738F` | `#5EADD5` | `#FFC55E` | `#D4B984` | `#5E85F9` |
| `Surface/Brand/Primary/Pressed` | `#D05159` | `#FC98AB` | `#91C7E3` | `#FFD88D` | `#E1CFAB` | `#91ACFB` |

</details>

### Status (18)

*Feedback messages, inline alerts, validation.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Status/Error-Strong/Default` | `#B32730` | `#E89597` | |
| `Color/Surface/Status/Error-Strong/Hover` | `#881E24` | `#EFB9BB` | |
| `Color/Surface/Status/Error-Strong/Pressed` | `#5E1519` | `#F6DCDD` | |
| `Color/Surface/Status/Error/Default` | `#FBEEEE` | `#881E24` | |
| `Color/Surface/Status/Error/Hover` | `#F6DCDD` | `#B32730` | |
| `Color/Surface/Status/Error/Pressed` | `#EFB9BB` | `#DC3741` | |
| `Color/Surface/Status/Information-Strong/Default` | `#006591` | `#8DAFCE` | |
| `Color/Surface/Status/Information-Strong/Hover` | `#004C6D` | `#B4C9DD` | |
| `Color/Surface/Status/Information-Strong/Pressed` | `#00344B` | `#DAE4ED` | |
| `Color/Surface/Status/Information/Default` | `#EDF1F6` | `#00344B` | |
| `Color/Surface/Status/Success-Strong/Default` | `#006D31` | `#8DB596` | |
| `Color/Surface/Status/Success-Strong/Hover` | `#005225` | `#B4CCBA` | |
| `Color/Surface/Status/Success-Strong/Pressed` | `#00391A` | `#DAE5DC` | |
| `Color/Surface/Status/Success/Default` | `#EDF2EE` | `#00391A` | |
| `Color/Surface/Status/Warning-Strong/Default` | `#7F561C` | `#E69B33` | |
| `Color/Surface/Status/Warning-Strong/Hover` | `#604015` | `#FFB868` | |
| `Color/Surface/Status/Warning-Strong/Pressed` | `#422C0E` | `#FFDCBE` | |
| `Color/Surface/Status/Warning/Default` | `#FFEEE0` | `#422C0E` | |

### Score (4)

*Score tag backgrounds only. Diamond highest, Bronze lowest.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Score/Bronze` | `#FFEEE0` | `#604015` | |
| `Color/Surface/Score/Diamond` | `#E3F8FF` | `#005875` | |
| `Color/Surface/Score/Gold` | `#FFF6D6` | `#826C1A` | |
| `Color/Surface/Score/Silver` | `#E9EEF5` | `#1E3C6B` | |

### Data visualisation (22)

*Charts and graphs only — never product UI.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Data/Categorical/1` | `#40559C` | `#5C73BC` | |
| `Color/Surface/Data/Categorical/2` | `#EE9D45` | `#E39C4F` | |
| `Color/Surface/Data/Categorical/3` | `#8FB875` | `#8FB875` | |
| `Color/Surface/Data/Categorical/4` | `#96CBEB` | `#A2C8DE` | |
| `Color/Surface/Data/Categorical/5` | `#BE5324` | `#CE6F46` | |
| `Color/Surface/Data/Categorical/Disabled` | `#DDDDDD` | `#DDDDDD` | |
| `Color/Surface/Data/Diverging/1` | `#4575B4` | `#4575B4` | |
| `Color/Surface/Data/Diverging/2` | `#74ADD1` | `#74ADD1` | |
| `Color/Surface/Data/Diverging/3` | `#ABD9E9` | `#ABD9E9` | |
| `Color/Surface/Data/Diverging/4` | `#E0F3F8` | `#E0F3F8` | |
| `Color/Surface/Data/Diverging/5` | `#FEE090` | `#FEE090` | |
| `Color/Surface/Data/Diverging/6` | `#FDAE61` | `#FDAE61` | |
| `Color/Surface/Data/Diverging/7` | `#F46D43` | `#F46D43` | |
| `Color/Surface/Data/Diverging/8` | `#D73027` | `#023858` | |
| `Color/Surface/Data/Sequential/1` | `#ECE7F2` | `#ECE7F2` | |
| `Color/Surface/Data/Sequential/2` | `#D0D1E6` | `#D0D1E6` | |
| `Color/Surface/Data/Sequential/3` | `#A6BDDB` | `#A6BDDB` | |
| `Color/Surface/Data/Sequential/4` | `#74A9CF` | `#74A9CF` | |
| `Color/Surface/Data/Sequential/5` | `#3690C0` | `#3690C0` | |
| `Color/Surface/Data/Sequential/6` | `#0570B0` | `#0570B0` | |
| `Color/Surface/Data/Sequential/7` | `#045A8D` | `#045A8D` | |
| `Color/Surface/Data/Sequential/8` | `#023858` | `#023858` | |

### Constant (13)

*Fixed colours and overlays that ignore brand.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Constant/Black/Default` | `#000000` | `#15171E` | |
| `Color/Surface/Constant/Black/Hover` | `#323232` | `#3D4459` | |
| `Color/Surface/Constant/Black/Pressed` | `#4B4B4B` | `#525A76` | Brand-variant — see below |
| `Color/Surface/Constant/Black/Transparent/Strong/Default` | `#00000080` | `#00000080` | |
| `Color/Surface/Constant/Black/Transparent/Strong/Hover` | `#00000099` | `#00000099` | |
| `Color/Surface/Constant/Black/Transparent/Strong/Pressed` | `#000000b2` | `#000000b2` | |
| `Color/Surface/Constant/Black/Transparent/Subdued/Default` | `#32323200` | `#32323200` | |
| `Color/Surface/Constant/Black/Transparent/Subdued/Hover` | `#32323233` | `#32323233` | |
| `Color/Surface/Constant/Black/Transparent/Subdued/Pressed` | `#3232324d` | `#3232324d` | |
| `Color/Surface/Constant/White/Default` | `#FFFFFF` | `#F8F8FA` | |
| `Color/Surface/Constant/White/Disabled` | `#4B4B4B` | `#3D4459` | |
| `Color/Surface/Constant/White/Hover` | `#E0E0E0` | `#C9CDDB` | |
| `Color/Surface/Constant/White/Pressed` | `#AEAEAE` | `#979EB5` | |

<details>
<summary>Brand variance — 1 token varies across the six brands (values below)</summary>

**Light**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Surface/Constant/Black/Pressed` | `#4B4B4B` | `#4B4B4B` | `#323232` | `#4B4B4B` | `#4B4B4B` | `#4B4B4B` |

**Dark**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Surface/Constant/Black/Pressed` | `#525A76` | `#525A76` | `#3D4459` | `#525A76` | `#525A76` | `#525A76` |

</details>

### Transparent (5)

*Transparent and inverted-transparent scrims.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Transparent-Inverted/Hover` | `#FFFFFF1a` | `#292D3B1a` | |
| `Color/Surface/Transparent-Inverted/Pressed` | `#FFFFFF33` | `#292D3B33` | |
| `Color/Surface/Transparent/Default` | `#32323200` | `#15171E00` | |
| `Color/Surface/Transparent/Hover` | `#3232321a` | `#F8F8FA1a` | |
| `Color/Surface/Transparent/Pressed` | `#32323233` | `#F8F8FA33` | |

### On-Brand / On-Primary / On-Secondary (7)

*Elements sitting on brand, primary or secondary backgrounds.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/On-Brand/Disabled` | `#FFFFFF80` | `#F8F8FA80` | |
| `Color/Surface/On-Brand/Hover` | `#FFFFFFe5` | `#F8F8FAe5` | |
| `Color/Surface/On-Brand/Pressed` | `#FFFFFFcc` | `#F8F8FAcc` | |
| `Color/Surface/On-Primary/Transparent/Hover` | `#FFFFFF33` | `#F8F8FA33` | |
| `Color/Surface/On-Primary/Transparent/Pressed` | `#FFFFFF4d` | `#F8F8FA33` | |
| `Color/Surface/On-Secondary/Transparent/Hover` | `#32323233` | `#F8F8FA33` | |
| `Color/Surface/On-Secondary/Transparent/Pressed` | `#3232324d` | `#F8F8FA33` | |

### Interactive & Active (9)

*Hover and pressed states, active selections.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Accent/Light/Default` | `#FCE6E7` | `#2E0000` | Brand-variant — see below |
| `Color/Surface/Active/Default` | `#FCE6E7` | `#2E0000` | Brand-variant — see below |
| `Color/Surface/Active/Hover` | `#F8C3C6` | `#3F0204` | Brand-variant — see below |
| `Color/Surface/Active/Pressed` | `#F3949A` | `#520408` | Brand-variant — see below |
| `Color/Surface/Interactive/Hover` | `#E0E0E0` | `#3D4459` | |
| `Color/Surface/Interactive/Pressed` | `#AEAEAE` | `#525A76` | |
| `Color/Surface/Interactive/Selected/Default` | `#4B4B4B` | `#AFB5C8` | |
| `Color/Surface/Interactive/Selected/Hover` | `#323232` | `#E3E5ED` | |
| `Color/Surface/Interactive/Selected/Pressed` | `#000000` | `#F8F8FA` | |

<details>
<summary>Brand variance — 4 tokens vary across the six brands (values below)</summary>

**Light**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Surface/Accent/Light/Default` | `#FCE6E7` | `#FFECEF` | `#E6F2F8` | `#FFF9EB` | `#F8F4EB` | `#C4D4F7` |
| `Surface/Active/Default` | `#FCE6E7` | `#FFECEF` | `#E6F2F8` | `#FFF9EB` | `#F8F4EB` | `#C4D4F7` |
| `Surface/Active/Hover` | `#F8C3C6` | `#FFC2CD` | `#C2E0EF` | `#FFEABC` | `#EEE4D0` | `#C2D0FD` |
| `Surface/Active/Pressed` | `#F3949A` | `#FC98AB` | `#91C7E3` | `#FFD88D` | `#E1CFAB` | `#91ACFB` |

**Dark**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Surface/Accent/Light/Default` | `#2E0000` | `#42000F` | `#003855` | `#400D00` | `#54411B` | `#001B6E` |
| `Surface/Active/Default` | `#2E0000` | `#42000F` | `#003855` | `#400D00` | `#54411B` | `#001B6E` |
| `Surface/Active/Hover` | `#3F0204` | `#680020` | `#00476C` | `#702500` | `#6A5222` | `#00238C` |
| `Surface/Active/Pressed` | `#520408` | `#890031` | `#005986` | `#9F4600` | `#84662A` | `#002BAE` |

</details>

### Decorative (2)

*Illustrations and decorative accents. Not semantic states.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Decorative/Red/Default` | `#DC3741` | `#E26C71` | |
| `Color/Surface/Decorative/Yellow/Default` | `#FFB868` | `#FFB868` | |

### base (15)

*General component fills. Start here for most product UI.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Surface/Dark/Default` | `#959595` | `#979EB5` | |
| `Color/Surface/Default/Default` | `#FFFFFF` | `#292D3B` | |
| `Color/Surface/Default/Hover` | `#F9F9F9` | `#3D4459` | |
| `Color/Surface/Default/Inverted/Default` | `#323232` | `#E3E5ED` | |
| `Color/Surface/Default/Pressed` | `#EEEEEE` | `#525A76` | |
| `Color/Surface/Disabled` | `#E0E0E0` | `#525A76` | |
| `Color/Surface/Light/Default` | `#F9F9F9` | `#525A76` | |
| `Color/Surface/Light/Hover` | `#EEEEEE` | `#68708C` | |
| `Color/Surface/Light/Pressed` | `#E0E0E0` | `#7F87A0` | |
| `Color/Surface/Light/Transparent/Default` | `#00000008` | `#68708Cbf` | |
| `Color/Surface/Light/Transparent/Hover` | `#00000012` | `#7F87A09c` | |
| `Color/Surface/Light/Transparent/Pressed` | `#0000001f` | `#979EB5d4` | |
| `Color/Surface/Subdued/Default` | `#EEEEEE` | `#3D4459` | |
| `Color/Surface/Subdued/Hover` | `#E0E0E0` | `#525A76` | |
| `Color/Surface/Subdued/Pressed` | `#C7C7C7` | `#68708C` | |
