Text styles for all GSL products, set in `Cera SL sys`. Sizes and line heights in px. Apply these as styles rather than setting font properties by hand.

## Overview

*Which family to use — see Semantic usage below for how the specific size within a family gets chosen.*

| Family   | Use for                                                                                                                                                                 |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Display  | Not observed in real product usage — see flag below before treating this as "hero-only"                                                                                 |
| Headline | A small set of sizes (22/24/28) applied either to a section/module header or to a price-style primary number — see the mechanism below, not a fixed size-per-level rule |
| Body     | The default text family — covers page/card titles, key facts, captions, and labels alike, sized by local emphasis rather than hierarchy depth                           |

## Semantic usage

*Bold vs Regular within any size is an emphasis choice, not a hierarchy signal. Underlined variants (Body only) mark inline interactive/link text within body copy — never apply underline decoration outside of a link.*

Token choice here is **not** a fixed page hierarchy ladder (no H1→H5-style mapping holds up against real screens). Size is chosen per block, based on two things: how prominent an element needs to look next to its immediate neighbors, and how much room its own container has. There's no formula that derives one exact token from those two factors — for a component with no existing precedent elsewhere in the product, this is a judgment call, not a lookup.

**Open question:** see [typography-usage-audit.md](typography-usage-audit.md) for the real-screen findings this is based on, concrete precedent pairings for known components, and open questions (including whether Display is genuinely unused or just unsampled in a hero context). Kept separate since it's exploratory research, not a validated ruleset.

## Tokens

### Display (6)

| Style | Size | Line height | Weight | Decoration |
| --- | --- | --- | --- | --- |
| `display/57/bold` | 57 | 64 | Bold | — |
| `display/57/regular` | 57 | 64 | Regular | — |
| `display/45/bold` | 45 | 52 | Bold | — |
| `display/45/regular` | 45 | 52 | Regular | — |
| `display/36/bold` | 36 | 44 | Bold | — |
| `display/36/regular` | 36 | 44 | Regular | — |

### Headline (10)

| Style | Size | Line height | Weight | Decoration |
| --- | --- | --- | --- | --- |
| `headline/32/bold` | 32 | 40 | Bold | — |
| `headline/32/regular` | 32 | 40 | Regular | — |
| `headline/28/bold` | 28 | 36 | Bold | — |
| `headline/28/regular` | 28 | 36 | Regular | — |
| `headline/24/bold` | 24 | 32 | Bold | — |
| `headline/24/regular` | 24 | 32 | Regular | — |
| `headline/22/bold` | 22 | 28 | Bold | — |
| `headline/22/regular` | 22 | 28 | Regular | — |
| `headline/20/bold` | 20 | 26 | Bold | — |
| `headline/20/regular` | 20 | 26 | Regular | — |

### Body (16)

| Style | Size | Line height | Weight | Decoration |
| --- | --- | --- | --- | --- |
| `body/16/bold` | 16 | 24 | Bold | — |
| `body/16/bold underlined` | 16 | 24 | Bold | underline |
| `body/16/regular` | 16 | 24 | Regular | — |
| `body/16/regular underlined` | 16 | 24 | Regular | underline |
| `body/14/bold` | 14 | 20 | Bold | — |
| `body/14/bold underlined` | 14 | 20 | Bold | underline |
| `body/14/regular` | 14 | 20 | Regular | — |
| `body/14/regular underlined` | 14 | 20 | Regular | underline |
| `body/12/bold` | 12 | 16 | Bold | — |
| `body/12/bold underlined` | 12 | 16 | Bold | underline |
| `body/12/regular` | 12 | 16 | Regular | — |
| `body/12/regular underlined` | 12 | 16 | Regular | underline |
| `body/11/bold` | 11 | 16 | Bold | — |
| `body/11/bold underlined` | 11 | 16 | Bold | underline |
| `body/11/regular` | 11 | 16 | Regular | — |
| `body/11/regular underlined` | 11 | 16 | Regular | underline |
