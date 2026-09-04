## Overview

*Which family to use. See Semantic usage below for the specific token within a family, and Tokens for exact values.*

| Family | Use for | Don't use for |
| --- | --- | --- |
| `Scales/Energy` | Energy Performance Class (DPE) label fills — A++ through G, per the Energy tag component | CO2 visualisation (→ `CO2`); any general product UI colour |
| `Scales/CO2` | CO2 emission scale data visualisation fills — a sequential blue palette | Energy class labels (→ `Energy`); general data visualisation (→ `Surface/Data`) |

## Semantic usage

### Energy

*Use only inside the Energy tag component. Always match the token to the actual DPE class from the listing data — never estimate or choose by colour preference.*

| Token | DPE class | Country availability |
| --- | --- | --- |
| `Scales/Energy/Green100` | A (or A++ in DE/AT scale) | All |
| `Scales/Energy/Green200` | B (or A+ in DE/AT scale) | All |
| `Scales/Energy/Green300` | C (or A in DE/AT scale) | All |
| `Scales/Energy/Green400` | D (or B in DE/AT scale) | All |
| `Scales/Energy/Yellow100` | E (or C in DE/AT scale) | All |
| `Scales/Energy/Yellow200` | F (or D in DE/AT scale) | All |
| `Scales/Energy/Orange100` | G (or E in DE/AT scale) | All |
| `Scales/Energy/Orange200` | F in DE/AT scale | DE/AT only |
| `Scales/Energy/Red100` | G in DE/AT scale | DE/AT only |
| `Scales/Energy/Red200` | H in DE/AT scale | DE/AT only |
| `Scales/Energy/Red300` | I in DE/AT scale (if applicable) | DE/AT only |
| `Scales/Energy/Blue100` | Special class (varies by country regulation) | Country-specific |

### CO2

*Sequential palette for CO2 emission visualisation only. Use Blue100 for the lowest emission value and Blue700 for the highest — never reverse the scale.*

| Token | When to use |
| --- | --- |
| `Scales/CO2/Blue100` | Lowest CO2 emission value in the scale |
| `Scales/CO2/Blue200–600` | Intermediate steps — assign in order, low to high |
| `Scales/CO2/Blue700` | Highest CO2 emission value in the scale |

## Tokens

### Scales — Energy (12)

*Energy Performance Class labels (A++ to G) only.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Scales/Energy/Blue100` | `#00ADEF` | `#56B3D6` | |
| `Color/Scales/Energy/Green100` | `#078748` | `#34805A` | |
| `Color/Scales/Energy/Green200` | `#60AD2E` | `#74A565` | |
| `Color/Scales/Energy/Green300` | `#8EC120` | `#A2C8DE` | |
| `Color/Scales/Energy/Green400` | `#CBDA0F` | `#D3DD76` | |
| `Color/Scales/Energy/Orange100` | `#F1C502` | `#EACC6E` | |
| `Color/Scales/Energy/Orange200` | `#EBA902` | `#DFAF63` | |
| `Color/Scales/Energy/Red100` | `#E38102` | `#D18B55` | |
| `Color/Scales/Energy/Red200` | `#D74202` | `#BB5240` | |
| `Color/Scales/Energy/Red300` | `#C40201` | `#AD3434` | |
| `Color/Scales/Energy/Yellow100` | `#F6ED02` | `#F3F07B` | |
| `Color/Scales/Energy/Yellow200` | `#F5DF02` | `#F3E477` | |

### Scales — CO2 (7)

*CO2 emission scale visualisation only.*

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Scales/CO2/Blue100` | `#91D9F9` | `#B5D1E8` | |
| `Color/Scales/CO2/Blue200` | `#80BCDD` | `#9AB4CF` | |
| `Color/Scales/CO2/Blue300` | `#70A0C2` | `#7F97B5` | |
| `Color/Scales/CO2/Blue400` | `#587598` | `#5D7294` | |
| `Color/Scales/CO2/Blue500` | `#47587C` | `#4D6184` | |
| `Color/Scales/CO2/Blue600` | `#363B60` | `#3B4E73` | |
| `Color/Scales/CO2/Blue700` | `#1F1238` | `#283A61` | |
