# Spacing and sizing usage audit

_Human-facing audit only — this is **not** the AI-facing ruleset. It records how
`Spacing/*` and `Sizing/*` are actually used in `gsl-core-web-design-system`,
and the mechanical verification of the rules `spacing-tokens.md` states. An AI
agent should read [spacing-rules-ai.md](spacing-rules-ai.md); this file holds
the evidence._

## Why this exists

`spacing-tokens.md` carried confident guidance — a four-layer model, a
container-padding table, a page-rhythm-by-viewport table, and four rules — none
of which had been checked against anything. That is the same shape of problem the
colour docs had: plausible, unverified, and impossible for an agent to trust.

Two of the four rules are mechanically checkable from component tokens. This pass
checks them.

Extracted by
[scripts/extract_spacing_usage.py](../scripts/extract_spacing_usage.py); ledger in
[spacing/spacing-usage-ledger.md](spacing-usage-ledger.md).

## Headline result: the rules hold

| Rule | Result |
| --- | --- |
| Page-rhythm tokens (48+) never used inside a component | **0 violations** across all 60 component token files |
| An inner gap never exceeds its container's padding | **0 violations** across the 24 components that have both |

This is worth stating plainly because it is the opposite of what the colour pass
found. The spacing rules were written without verification, and they turned out
to be **accurate descriptions of what the code already does**. They are now
verified rather than asserted, and the check is reproducible.

The two remaining rules — "never hardcode a pixel literal" and "don't override a
component's internal padding via CSS" — are about product code, which is outside
this monorepo. Still unverifiable here.

## The scale splits cleanly at 32

| Range | Component bindings | Meaning |
| --- | --- | --- |
| `2` – `32` (+ `None`) | all 217 | component-internal spacing |
| `40` | 0 component tokens; direct use in `CoachMark`, charts | boundary case |
| `48`, `56`, `64`, `80`, `128`, `256` | **0** | page rhythm — product pages only |

**The six unconsumed tokens are not dead.** They are exactly the tokens the doc
reserves for macro layout, and no component touches them. The absence *is* the
rule being obeyed. This mirrors typography, where the `display` scale has no
component consumer for the same reason.

`Spacing/40` sits on the boundary: no component token binds it, but `CoachMark`
and the chart components use it directly in `.tsx`. Its documented purpose
("extended separation between independent form sections") is page-level, so the
direct uses are the anomaly, not the token.

### Most-used spacing tokens

| Token | px | Components |
| --- | --- | --- |
| `Spacing/8` | 8 | 36 |
| `Spacing/16` | 16 | 27 |
| `Spacing/4` | 4 | 23 |
| `Spacing/12` | 12 | 14 |
| `Spacing/32` | 32 | 9 |
| `Spacing/2` | 2 | 5 |

`Spacing/8`, `16` and `4` account for most component spacing. `Spacing/20` is
bound by a single component — the thinnest justification in the scale.

## `Spacing/56` has no documented purpose

It appears in the token table and in no usage note, no layer, and no applied
pattern. No component binds it, and neither page-rhythm table references it. It
is the one token in the scale with nothing said about it anywhere.

→ Flagged, not resolved: either give it a purpose or retire it.

## `Sizing/*` was entirely undocumented

43 tokens, 98 component bindings, and **no doc page existed**. It was
absent from the category index too.

It is a different kind of scale from `Spacing`:

- Not geometric — `142`, `204`, `294` sit alongside `144`, `160`, `288`.
- Low reuse — over half its tokens are bound by exactly one component.
- Mostly variant maps: `avatar`'s ten size steps, `modal.predefinedWidth.*`,
  `progressBar` bar thicknesses.

**It is not a design property.** Confirmed by Gabriel and by the Figma tokens
registry, which defines six families — Border Width, Breakpoint, Color, Grid,
Radius, Spacing — and no Sizing. It is a code-side bookkeeping layer that names
fixed pixel dimensions so repeated values are linked and changeable in one place.
That explains its shape: it is a ledger of dimensions the designs happened to
need, not a scale anyone designed.

It is a catalogue of concrete dimensions, not a rhythm. Now documented at
[sizing-tokens.md](../sizing/sizing-tokens.md).

**Six sizing tokens have no consumer** — `14`, `36`, `142`, `204`, `288`, `294`.
Unlike spacing, there is no page-level explanation available: a dimension scale
is only ever consumed by components. These are the likeliest genuinely dead
tokens found in any pass so far. Confirm against Figma before removing.

## The "Primitive tier" claim

`spacing-tokens.md` opened by asserting spacing belongs to the "`Primitive`
architectural tier, not the `Brand` tier". That term appears nowhere in the code
repo — it is presumably Figma variable-collection naming.

The *structural* claim is true and verifiable: spacing is brand-independent,
defined once in `shared/figma/spacings.json`, identical for every brand and both
modes. The page now says that, without the unverifiable label.

## Not verified

- The **container-padding** and **page-rhythm-by-viewport** tables. Both describe
  product-page composition, which lives outside this monorepo. They remain
  plausible and unchecked — the same caveat the colour audit carries for
  real-page compliance.
- Whether `Spacing/40`'s direct uses in `CoachMark` and the chart components are
  appropriate.

## Open

- **`Spacing/56`** — purpose or retirement?
- **The six unconsumed `Sizing` tokens** — dead, or reserved for something in
  Figma?
- **`Spacing/20`**, bound by one component — keep, or fold into `16`/`24`?
