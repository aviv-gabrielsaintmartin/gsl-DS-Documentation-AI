## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for |
| --- | --- | --- |
| `Surface/base` | The default starting point for most components — cards, sheets, standard containers | Anything with a more specific match below |
| `Surface/Brand` | CTAs and primary/secondary brand-identity fills | Non-branded interactive elements (→ `Interactive`) |
| `Surface/Status` | Feedback messages, inline alerts, validation states (error/warning/success/info) | Persistent quality tiers (→ `Score`) |
| `Surface/Score` | Advertiser/listing quality tier badges (Diamond–Bronze) | Status/feedback states (→ `Status`) |
| `Surface/Interactive & Active` | Generic hover/pressed/selected/active states with no other semantic role | Elements with a dedicated family already (Status, Brand, Score) |
| `Surface/Constant` | Fixed black/white fills that must ignore brand and light/dark mode entirely | Anything that should re-theme (→ `base`, `Default/Inverted`) |
| `Surface/Transparent` | See-through washes with no solid colour, for subtle interaction feedback | Visible/solid state changes (→ `Interactive`) |
| `Surface/On-Brand / On-Primary / On-Secondary` | An element's own fill when it sits on top of a brand/primary/secondary surface | The brand/primary/secondary surface itself |
| `Surface/Data visualisation` | Charts and graphs only | Product UI, ever — even if a colour looks right |
| `Surface/Decorative` | Fixed accent fills for non-semantic decorative elements — rating-star fills, edit-highlight backgrounds — accent colour with no state meaning | Semantic states (→ `Status`, `Active`, `Score`); illustration/avatar fills (→ Symbol family) |

## Semantic usage

### Brand

| Token | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Brand/Primary` | Main brand-coloured CTA fill — primary buttons, key actions, one per screen/section | Secondary or supporting fills (→ `Surface/Brand/Secondary`) |
| `Surface/Brand/Secondary` | Secondary brand-associated fill that stays constant across all six brands (not tinted) — dark accents, secondary badges | Primary CTAs (→ `Surface/Brand/Primary`) |

### Status

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Status/Error` | Light error background — feedback message body, inline validation banner | Solid/high-contrast error fills (→ `Error-Strong`) |
| `Surface/Status/Error-Strong` | Solid, high-contrast error fill — error badges, icon containers, anything needing strong emphasis | Banner/message backgrounds (→ `Error`) |
| `Surface/Status/Information` | Light informational background — tips, neutral announcements | Solid info fills (→ `Information-Strong`) |
| `Surface/Status/Information-Strong` | Solid, high-contrast info fill | Banner/message backgrounds (→ `Information`) |
| `Surface/Status/Success` | Light success background — confirmation banners | Solid success fills (→ `Success-Strong`) |
| `Surface/Status/Success-Strong` | Solid, high-contrast success fill | Banner/message backgrounds (→ `Success`) |
| `Surface/Status/Warning` | Light warning background | Solid warning fills (→ `Warning-Strong`) |
| `Surface/Status/Warning-Strong` | Solid, high-contrast warning fill | Banner/message backgrounds (→ `Warning`) |

*General rule across all four: `-Strong` is a contrast/weight choice (solid fill vs. light wash), not a severity escalation — don't reach for `-Strong` just because a message feels more urgent.*

### Score

| Token | When to use |
| --- | --- |
| `Surface/Score/Diamond` | Highest advertiser/listing quality tier |
| `Surface/Score/Gold` | Second-highest tier |
| `Surface/Score/Silver` | Third tier |
| `Surface/Score/Bronze` | Lowest tier |

*Score tag backgrounds only. Never substitute for `Surface/Status/*` — Score is a tier ranking, not a state.*

### Data visualisation

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Data/Categorical` | Distinct, unordered categories in a chart (up to 5 series) | Ordered/magnitude data (→ Sequential) |
| `Surface/Data/Categorical/Disabled` | A categorical series that's toggled off/inactive in a legend | Any in-use series |
| `Surface/Data/Sequential` | Data with a single ordered magnitude, low to high (e.g. a heatmap of one metric) | Data with a meaningful zero-crossing (→ Diverging) |
| `Surface/Data/Diverging` | Data with a meaningful midpoint — deviation above/below a baseline (e.g. profit/loss) | Simple ordered magnitude (→ Sequential) |

*Charts and graphs only — never product UI, regardless of how well a colour happens to fit.*

### Constant

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Constant/Black` | Fixed black fill and its interaction states, ignoring brand and light/dark mode | Anything that should re-theme (→ `Surface/Default/Inverted`) |
| `Surface/Constant/Black/Transparent/Strong` | Strong black scrim/overlay, fixed opacity regardless of mode | Subtle overlays (→ `Transparent/Subdued`) |
| `Surface/Constant/Black/Transparent/Subdued` | Light black scrim/overlay, fixed opacity regardless of mode | Strong overlays (→ `Transparent/Strong`) |
| `Surface/Constant/White` | Fixed white fill and its interaction states, ignoring brand and light/dark mode | Anything that should re-theme (→ `Surface/Default`) |

### Transparent

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Transparent` | A see-through fill over a light/default-mode background — subtle hover/press wash with no solid colour | Fills over dark/inverted content (→ `Transparent-Inverted`) |
| `Surface/Transparent-Inverted` | A see-through fill over a dark/inverted background | Fills over standard-mode content (→ `Transparent`) |

### On-Brand / On-Primary / On-Secondary

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Surface/On-Brand` | An element's interaction-state fill when it sits directly on a brand-coloured surface | Elements on the default page background |
| `Surface/On-Primary/Transparent` | A transparent interaction wash for an element on a primary-coloured fill (e.g. hover on an icon inside a primary button) | Solid on-primary fills — this family is transparency-only |
| `Surface/On-Secondary/Transparent` | Same, on a secondary-coloured fill | Solid on-secondary fills |

### Interactive & Active

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Accent/Light` | A light, brand-tinted accent fill for highlighting content without implying selection | Selected/active state (→ `Active`) — see flag below |
| `Surface/Active` | The fill for a currently active/highlighted item (e.g. an active filter chip's background) | Permanent selection state (→ `Interactive/Selected`) |
| `Surface/Interactive` | Generic hover/pressed fill for any interactive element with no other semantic role | Elements with a dedicated state family (Status, Active, Selected) |
| `Surface/Interactive/Selected` | The fill for an item in a persisted selected state (e.g. a chosen radio card, toggled filter) | Momentary active/highlight (→ `Active`) |

**Open question:** `Accent/Light/Default` and `Active/Default` currently resolve to the identical hex in both Light and Dark (`#FCE6E7` / `#2E0000`). Unclear whether these are meant to be the same token under two names, or should diverge — an agent currently can't tell which is "correct" for a new use case since both produce the same result. Needs confirmation before this ambiguity is resolved.

### Decorative

| Token | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Decorative/Red` | A fixed accent fill for a non-semantic decorative element — e.g. a rating-star fill, or the background marking an edited/changed portion of content | Any state that maps to Status/Active/Score (→ use that family); illustration or avatar fills (→ Symbol family) |
| `Surface/Decorative/Yellow` | Same use cases as `Red`, when a second decorative accent is needed (e.g. a two-tone rating display) | Same as `Red` |

*Decorative tokens carry brand/visual accent, not state. If an element's colour is meant to communicate something (error, active, tier), that's a missed semantic case, not a Decorative one.*

**Open question:** the boundary between `Decorative` and the semantic state families (`Status`, `Active`, `Score`) hasn't been stress-tested against a real ambiguous case yet — flagged in an earlier review pass as still too loosely defined, pending a concrete example that would pin it down.

### base

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Surface/Default` | The default fill for most components — cards, sheets, standard containers. Start here. | Page-level canvas (→ `Background/Default`) |
| `Surface/Default/Inverted` | A component fill that should flip against the page's light/dark mode (e.g. a dark card in light mode) | Fixed-colour needs regardless of mode (→ `Constant`) |
| `Surface/Light` | A lighter component fill for subtle recessed containers within a component | Page-level background (→ `Background/Light`) |
| `Surface/Light/Transparent` | A translucent, very subtle wash — barely-visible hover/press feedback | Visible state changes (→ `Surface/Interactive`) |
| `Surface/Subdued` | A muted component fill — de-emphasised containers | Disabled state (→ `Surface/Disabled`) |
| `Surface/Disabled` | The fill for a disabled component | Muted-but-interactive containers (→ `Subdued`) |
| `Surface/Dark` | A dark, high-contrast component fill | General component use (→ `Default`) |

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
