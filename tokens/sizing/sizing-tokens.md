Fixed component dimensions — control heights, avatar and icon sizes, image
thumbnails, panel widths. Values in px.

> **This page is new.** `Sizing/*` had no documentation before this pass despite
> 43 tokens and 98 component bindings. Content is derived from real usage:
> [spacing/spacing-usage-ledger.md](../spacing/spacing-usage-ledger.md). Rules:
> [spacing-rules-ai.md](../spacing/spacing-rules-ai.md).

## It does not exist in Figma — and that is not an oversight

`Sizing` is **not a design property**. The Figma tokens registry defines six
families — Border Width, Breakpoint, Color, Grid, Radius, Spacing — and Sizing is
not among them. Designers do not pick a Sizing token, and should not be asked to.

It exists only in code, for a reason that has no Figma equivalent:

- **In Figma**, a 48px-tall input simply *is* 48px tall. The number lives on the
  component; change it there and every instance follows. The value and the thing
  are the same object.
- **In code** they are separate. `height: 48px` in `TextField` and `height: 48px`
  in `Dropdown` are two unrelated numbers that happen to match. Nothing connects
  them, nothing tells you which 48s mean "control height" and which are
  coincidence, and changing control height means finding every one by hand.

`Sizing/48` gives the number a name so those uses are linked, searchable, and
changeable in one place. It is bookkeeping, not design.

**This is why it does not read like a good scale.** Colour, Spacing and Radius
are designed systems — someone chose the steps. Sizing is a *ledger*: a record of
whatever dimensions the designs happened to need. That is why `142`, `204` and
`294` sit beside `144`, `288` and `320`. Nobody designed that; it accumulated.

## Sizing is not Spacing

They look alike and are not interchangeable:

| | `Spacing/*` | `Sizing/*` |
| --- | --- | --- |
| Answers | how far apart? | how big? |
| Applies to | padding, gaps, margins | width, height, min-width |
| Shape | a rhythm scale — 17 steps, geometric | a dimension catalogue — 43 values, many bespoke |
| Reuse | `Spacing/8` used by 36 components | over half of `Sizing/*` is used by one component each |

A gap is `Spacing`. A control's height is `Sizing`. Getting this wrong produces
layouts that look right at one breakpoint and break at another.

## What it is actually used for

| Purpose | Typical tokens | Example |
| --- | --- | --- |
| Icon and glyph sizes | `16`, `20`, `24`, `32` | `chip`, `statusTag`, `accordion` chevrons |
| Control heights | `32`, `40`, `48` | `datePicker.height` = 48 |
| Avatar size ramp | `24`, `32`, `40`, `48`, `56`, `64`, `72`, `80`, `104`, `128` | `avatar` variant map |
| Image thumbnails | `48`, `80`, `144` | `cellContent.image` = 48 |
| Panel and field widths | `144`, `280`, `320`, `328`, `536`, `640`, `704`, `1120` | `modal.predefinedWidth.328` |
| Bar and indicator thicknesses | `4`, `8` | `progressBar`, `carousel.indicator` |

## Rules

- **Use `Sizing/*` only for a fixed width or height.** Never for padding, gaps
  or margins — those are `Spacing/*`.
- **Prefer the component.** Most of these tokens exist to express one
  component's variant map. If you are picking a `Sizing` token by hand you are
  probably rebuilding something that exists.
- **Designers do not need this page.** Specify dimensions in Figma as normal; a
  developer records them here. The one thing worth knowing is below.
- **Don't treat it as a scale.** It is not geometric and has no rhythm — `142`,
  `204`, `294` sit alongside `144`, `160`, `288`. Pick the value a design calls
  for; do not interpolate a "next step up".
- **Never hardcode a pixel literal** for a dimension the scale already covers.

## Tokens (43)

| Token | px | Components | Used by |
| --- | --- | --- | --- |
| `Sizing/2` | 2 | 1 | `slider` |
| `Sizing/4` | 4 | 4 | `buttonGroup`, `progressBar`, `slider`, `wizard` |
| `Sizing/6` | 6 | 1 | `slider` |
| `Sizing/8` | 8 | 4 | `carousel`, `progressBar`, `slider`, `wizard` |
| `Sizing/10` | 10 | 1 | `wizard` |
| `Sizing/12` | 12 | 2 | `slider`, `wizard` |
| `Sizing/14` | 14 | 0 | **no component** |
| `Sizing/16` | 16 | 5 | `badge`, `icon`, `progressBar`, `rating` +1 · direct: `Chip`, `StatusTag` |
| `Sizing/18` | 18 | 2 | `checkbox`, `slider` |
| `Sizing/20` | 20 | 2 | `icon`, `radio` · direct: `Accordion`, `Button` |
| `Sizing/24` | 24 | 10 | `avatar`, `badge`, `checkbox`, `icon` +6 · direct: `Accordion`, `ActionMenu` |
| `Sizing/28` | 28 | 1 | `toggle` |
| `Sizing/32` | 32 | 11 | `avatar`, `brandLogo`, `button`, `carousel` +7 · direct: `BrandLogo.tsx` |
| `Sizing/36` | 36 | 0 | **no component** |
| `Sizing/40` | 40 | 11 | `avatar`, `brandLogo`, `button`, `buttonGroup` +7 · direct: `DateCalendar`, `SelectCardGroup` |
| `Sizing/44` | 44 | 1 | `slider` |
| `Sizing/46` | 46 | 1 | `slider` |
| `Sizing/48` | 48 | 9 | `avatar`, `button`, `cellContent`, `counterField` +5 · direct: `unsafe` |
| `Sizing/52` | 52 | 2 | `slider`, `toggle` |
| `Sizing/56` | 56 | 1 | `avatar` |
| `Sizing/60` | 60 | 2 | `slider`, `wizard` |
| `Sizing/64` | 64 | 3 | `avatar`, `selectCardGroup`, `slider` |
| `Sizing/68` | 68 | 1 | `slider` |
| `Sizing/72` | 72 | 1 | `avatar` |
| `Sizing/80` | 80 | 1 | `avatar` |
| `Sizing/96` | 96 | 1 | `textArea` |
| `Sizing/104` | 104 | 1 | `avatar` |
| `Sizing/108` | 108 | 1 | `mediaUpload` |
| `Sizing/128` | 128 | 1 | `avatar` |
| `Sizing/142` | 142 | 0 | **no component** |
| `Sizing/144` | 144 | 2 | `counterField`, `infoState` |
| `Sizing/160` | 160 | 1 | `selectCardGroup` |
| `Sizing/204` | 204 | 0 | **no component** |
| `Sizing/256` | 256 | 1 | `tooltip` |
| `Sizing/280` | 280 | 5 | `datePicker`, `dropdown`, `slider`, `textArea` +1 |
| `Sizing/288` | 288 | 0 | **no component** |
| `Sizing/294` | 294 | 0 | **no component** |
| `Sizing/320` | 320 | 1 | `actionMenu` |
| `Sizing/328` | 328 | 1 | `modal` |
| `Sizing/536` | 536 | 1 | `modal` |
| `Sizing/640` | 640 | 1 | `modal` |
| `Sizing/704` | 704 | 1 | `modal` |
| `Sizing/1120` | 1120 | 1 | `modal` |

### What this costs, and the one thing worth knowing

Every unusual dimension a design specifies becomes a permanent entry here. The
result: 43 tokens, over half bound by exactly one component, six bound by none.
Look at the near-duplicates — `142`/`144`, `288`/`294` — those pairs are almost
certainly the same intent, measured twice.

So: when a dimension is not visually load-bearing, matching a value already in
the ledger keeps it small. Not a rule — just where the cost lands.

Six tokens — `14`, `36`, `142`, `204`, `288`, `294` — have no component
consumer. Unlike `Spacing`, there is no page-level explanation for these: a
dimension scale is only ever consumed by components. They are the likeliest
genuinely dead tokens in the system, but confirm against Figma before removing
any.
