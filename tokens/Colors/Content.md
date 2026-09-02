## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for |
| --- | --- | --- |
| `Content/base` | Text and icon fills for standard UI — the default starting point for all text colour decisions | Anything with a more specific match below |
| `Content/Status` | Text and icon colour inside or alongside a status state (error, warning, success, info) | Score tier labels (→ `Score`) |
| `Content/Score` | Text colour inside a Score tag (Diamond–Bronze tier labels) | Status/feedback text (→ `Status`) |

## Semantic usage

### base

*Bind all text and icon fills to these — never hardcode a colour value.*

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Content/Default` | Primary body text, labels, headings — the default for most text. Start here. | De-emphasised or disabled text (→ `Subdued`, `Light`, `Disabled`) |
| `Content/Default/Inverted` | Text on a dark/inverted background | Text on standard-mode backgrounds (→ `Default`) |
| `Content/Subdued` | Secondary or supporting text — metadata, captions, helper labels with lower visual priority | Disabled text (→ `Disabled`); primary body text (→ `Default`) |
| `Content/Light` | Tertiary text — timestamps, footnotes, low-emphasis annotations | Anything needing more than minimal contrast (→ `Subdued` or `Default`) |
| `Content/Disabled` | Text or icon on a disabled component | De-emphasised but interactive text (→ `Subdued`) |
| `Content/Active` | Text on an active/highlighted item | Selected/persisted state (→ `Interactive`) |
| `Content/Interactive` | Text or icon colour responding to hover/pressed/selected states with no other semantic role | Elements with a dedicated content family (Status, On-Primary, On-Secondary) |
| `Content/Interactive/Inverted` | Interactive-state text on a dark/inverted background | Standard-mode interactive text (→ `Interactive`) |
| `Content/On-Brand/Disabled` | Disabled text sitting directly on a brand-coloured surface | Enabled text on brand surfaces (→ `On-Primary`) |
| `Content/On-Primary` | Text or icon on a primary brand-coloured fill (e.g. label inside a primary button) | Text on secondary fills (→ `On-Secondary`) |
| `Content/On-Secondary` | Text or icon on a secondary brand-coloured fill | Text on primary fills (→ `On-Primary`) |
| `Content/Constant/Black` | Fixed near-black text, ignores brand and mode — always dark regardless of theme | Anything that should re-theme (→ `Default`) |
| `Content/Constant/White` | Fixed white text, ignores brand and mode — always light regardless of theme | Anything that should re-theme (→ `Default/Inverted`) |
| `Content/Constant/White/onDark` | Fixed white text specifically for a dark background context — slightly muted vs pure white | Standard dark-mode text (→ `Default` in dark mode) |

### Status

| Token root | When to use | Don't use for |
| --- | --- | --- |
| `Content/Status/Error` | Error text or icon — validation messages, failed states, inline field errors | Warning text the user should notice but not fix immediately (→ `Warning`) |
| `Content/Status/Error-Strong` | Stronger error emphasis — error text on a light error surface needing higher contrast | Standard error labels (→ `Error`) |
| `Content/Status/Error/Inverted` | Error text on a dark/error-strong surface | Error text on standard backgrounds (→ `Error`) |
| `Content/Status/Warning` | Warning text — prompts the user to review before continuing | Confirmed failures (→ `Error`) |
| `Content/Status/Warning-Strong` | Higher-contrast warning text on a light warning surface | Standard warning labels (→ `Warning`) |
| `Content/Status/Warning/Inverted` | Warning text on a dark/warning-strong surface | Warning text on standard backgrounds (→ `Warning`) |
| `Content/Status/Success` | Confirmation text — action completed, saved, uploaded | Ongoing neutral info (→ `Information`) |
| `Content/Status/Success-Strong` | Higher-contrast success text on a light success surface | Standard success labels (→ `Success`) |
| `Content/Status/Success/Inverted` | Success text on a dark/success-strong surface | Success text on standard backgrounds (→ `Success`) |
| `Content/Status/Information` | Informational text — tips, announcements, non-urgent notes | Actionable states (→ `Warning`, `Error`) |
| `Content/Status/Information-Strong` | Higher-contrast information text on a light info surface | Standard info labels (→ `Information`) |
| `Content/Status/Information/Inverted` | Information text on a dark/info-strong surface | Info text on standard backgrounds (→ `Information`) |

*General rule: `-Strong` is a contrast choice (higher emphasis on a light wash background), not a severity escalation. `/Inverted` is for text sitting on a solid status-coloured fill.*

### Score

| Token | When to use |
| --- | --- |
| `Content/Score/Diamond` | Text label inside a Diamond-tier Score tag |
| `Content/Score/Gold` | Text label inside a Gold-tier Score tag |
| `Content/Score/Silver` | Text label inside a Silver-tier Score tag |
| `Content/Score/Bronze` | Text label inside a Bronze-tier Score tag |

*Paired with the matching `Surface/Score/*` background. Never use for general status text — Score is a tier ranking label only.*

## Tokens

### base (27)

*Text and icon fills. Bind text fills to these — never hardcode.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Content/Active/Default` | `#323232` | `#F8F8FA` | |
| `Color/Content/Active/Pressed` | `#323232` | `#F8F8FA` | |
| `Color/Content/Constant/Black/Default` | `#323232` | `#292D3B` | |
| `Color/Content/Constant/White/Default` | `#FFFFFF` | `#FFFFFF` | |
| `Color/Content/Constant/White/onDark/Default` | `#E0E0E0` | `#E3E5ED` | |
| `Color/Content/Default/Default` | `#323232` | `#F8F8FA` | |
| `Color/Content/Default/Inverted/Default` | `#FFFFFF` | `#15171E` | |
| `Color/Content/Default/Inverted/Hover` | `#E0E0E0` | `#525A76` | |
| `Color/Content/Default/Inverted/Pressed` | `#C7C7C7` | `#68708C` | |
| `Color/Content/Disabled` | `#959595` | `#7F87A0` | |
| `Color/Content/Interactive/Default` | `#323232` | `#F8F8FA` | |
| `Color/Content/Interactive/Hover` | `#4B4B4B` | `#AFB5C8` | |
| `Color/Content/Interactive/Inverted/Default` | `#EEEEEE` | `#292D3B` | |
| `Color/Content/Interactive/Inverted/Hover` | `#E0E0E0` | `#AFB5C8` | |
| `Color/Content/Interactive/Inverted/Pressed` | `#C7C7C7` | `#525A76` | |
| `Color/Content/Interactive/Pressed` | `#000000` | `#E3E5ED` | |
| `Color/Content/Light/Default` | `#646464` | `#AFB5C8` | |
| `Color/Content/On-Brand/Disabled` | `#32323280` | `#292D3B80` | |
| `Color/Content/On-Primary/Default` | `#FFFFFF` | `#F8F8FA` | Brand-variant — see below |
| `Color/Content/On-Primary/Disabled` | `#FFFFFF99` | `#F8F8FA80` | Brand-variant — see below |
| `Color/Content/On-Primary/Hover` | `#FFFFFFcc` | `#F8F8FAcc` | Brand-variant — see below |
| `Color/Content/On-Primary/Pressed` | `#FFFFFFb2` | `#F8F8FAb2` | Brand-variant — see below |
| `Color/Content/On-Secondary/Default` | `#FFFFFF` | `#F8F8FA` | |
| `Color/Content/On-Secondary/Disabled` | `#FFFFFF99` | `#F8F8FA99` | |
| `Color/Content/On-Secondary/Hover` | `#FFFFFFcc` | `#F8F8FAcc` | |
| `Color/Content/On-Secondary/Pressed` | `#FFFFFFb2` | `#F8F8FAb2` | |
| `Color/Content/Subdued/Default` | `#4B4B4B` | `#C9CDDB` | |

<details>
<summary>Brand variance — 4 of 27 tokens vary across the six brands (values below)</summary>

**Light**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Content/On-Primary/Default` | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` | `#323232` | `#FFFFFF` | `#FFFFFF` |
| `Content/On-Primary/Disabled` | `#FFFFFF99` | `#FFFFFF99` | `#FFFFFF99` | `#32323280` | `#FFFFFF99` | `#FFFFFF99` |
| `Content/On-Primary/Hover` | `#FFFFFFcc` | `#FFFFFFcc` | `#FFFFFFcc` | `#323232cc` | `#FFFFFFcc` | `#FFFFFFcc` |
| `Content/On-Primary/Pressed` | `#FFFFFFb2` | `#FFFFFFb2` | `#FFFFFFb2` | `#323232b2` | `#FFFFFFb2` | `#FFFFFFb2` |

**Dark**

| Token | SeLoger | SeLoger Neuf | Logic Immo | Logic Immo Neuf | Belles Demeures | Meilleurs Agents |
| --- | --- | --- | --- | --- | --- | --- |
| `Content/On-Primary/Default` | `#F8F8FA` | `#15171E` | `#15171E` | `#15171E` | `#15171E` | `#F8F8FA` |
| `Content/On-Primary/Disabled` | `#F8F8FA80` | `#15171E99` | `#15171E99` | `#15171E99` | `#15171E99` | `#F8F8FA99` |
| `Content/On-Primary/Hover` | `#F8F8FAcc` | `#15171Ecc` | `#15171Ecc` | `#15171Ecc` | `#15171Ecc` | `#F8F8FAcc` |
| `Content/On-Primary/Pressed` | `#F8F8FAb2` | `#15171Eb2` | `#15171Eb2` | `#15171Eb2` | `#15171Eb2` | `#F8F8FAb2` |

</details>

### Status (14)

*Text and icon colours for status states.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Content/Status/Error-Strong/Default` | `#5E1519` | `#F6DCDD` | |
| `Color/Content/Status/Error/Default` | `#B32730` | `#E89597` | |
| `Color/Content/Status/Error/Hover` | `#881E24` | `#EFB9BB` | |
| `Color/Content/Status/Error/Inverted/Default` | `#E89597` | `#B32730` | |
| `Color/Content/Status/Error/Pressed` | `#5E1519` | `#F6DCDD` | |
| `Color/Content/Status/Information-Strong/Default` | `#00344B` | `#DAE4ED` | |
| `Color/Content/Status/Information/Default` | `#006591` | `#8DAFCE` | |
| `Color/Content/Status/Information/Inverted/Default` | `#8DAFCE` | `#006591` | |
| `Color/Content/Status/Success-Strong/Default` | `#00391A` | `#DAE5DC` | |
| `Color/Content/Status/Success/Default` | `#006D31` | `#8DB596` | |
| `Color/Content/Status/Success/Inverted/Default` | `#8DB596` | `#006D31` | |
| `Color/Content/Status/Warning-Strong/Default` | `#422C0E` | `#FFDCBE` | |
| `Color/Content/Status/Warning/Default` | `#7F561C` | `#E69B33` | |
| `Color/Content/Status/Warning/Inverted/Default` | `#E69B33` | `#7F561C` | |

### Score (4)

*Text colours for the Score tag only.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Content/Score/Bronze` | `#604015` | `#FFEEE0` | |
| `Color/Content/Score/Diamond` | `#005A78` | `#E3F8FF` | |
| `Color/Content/Score/Gold` | `#5E4E12` | `#FFF6D6` | |
| `Color/Content/Score/Silver` | `#3B3F4A` | `#E9EEF5` | |
