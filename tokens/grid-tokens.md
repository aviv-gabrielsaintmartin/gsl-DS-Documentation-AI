Column-grid setup per viewport size — column count, outer margin, gutter and computed column width.

`Count`, `Margin`, and `Gutter` have a confirmed code equivalent, matching design specifications across all seven tiers.

## Tokens (4)

| Token | Importable | XS | SM | MD | LG | XL | XXL | XXXL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Grid/Count` | no | 4 | 8 | 8 | 8 | 12 | 12 | 12 |
| `Grid/Margin` | yes | 16 | 32 | 32 | 32 | 80 | 80 | 80 |
| `Grid/Gutter` | yes | 16 | 16 | 16 | 16 | 24 | 24 | 24 |
| `Grid/Width` | no | 70 | 53 | 74 | 106 | 71.33 | 92.67 | 124.67 |

`Grid/Width` is a computed column width, which is why it carries fractional values at the larger sizes.

**Flag — unconfirmed:** these values existing in code confirms the _tokens_ are defined, not that a _grid layout system_ is built or in use. No layout component or asset currently implements column-grid behaviour, and we don't know whether any team is already consuming these values directly. An agent should not treat the presence of `Count`/`Margin`/`Gutter` as evidence that a sanctioned grid layout pattern exists to build against — using them today would mean assembling a layout from raw values, not applying an established component.
