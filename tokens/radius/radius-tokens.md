> **This page is evidence-based.** The **Used by** column is taken from real component bindings. Live-component evidence: [radius-usage-audit.md](radius-usage-audit.md).

Radius is brand-independent — the same five tokens resolve to the same values for every brand and both modes. It is the correct and only source for corner radius, as it is for spacing and border width. *(The earlier wording called this the "`Primitive` architectural tier"; that term appears nowhere in the code repo — presumably Figma variable-collection naming — so the structural claim is stated directly instead.)* Use for cards, buttons, inputs and any rounded container. Values in px.

## Semantic usage

| Token            | When to use                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `Radius/None`    | Square corners — flush/full-bleed surfaces and edge-docked elements, e.g. the borderless "floating banner" variant of Feedback message         |
| `Radius/4`       | Small surfaces — smaller cards (Card's `Radius=4` variant), and other compact components; also the fixed corner radius on chart bars           |
| `Radius/8`       | Mid-size rectangular containers and controls — standard cards (Card's `Radius=8` variant), Text Field, Snackbar, Text Button                   |
| `Radius/16`      | Larger containers — bigger cards (Card's `Radius=16` variant), Accordion, Coach mark                                                            |
| `Radius/Rounded` | Fully rounded / pill shape — filled/interactive controls: Button (incl. icon-only, which becomes a full circle), Tag, Chip. A clamp value (10000), not a literal radius, so it always resolves to a full capsule regardless of element height |

*Card literally exposes radius as a component variant (`Radius=4`, `Radius=8`, `Radius=16`) — confirmed directly, not inferred; see [Card](../../components/card/card.md#radius) for the size-to-radius mapping rule. It's not purely size-based: shape category (filled/interactive control vs. rectangular container) determines the tier at least as much as size — see [radius-usage-audit.md](radius-usage-audit.md) for the full live-component and live-page spot-check evidence, plus two related out-of-scope findings.*

## Tokens (5)

| Token | Value | Components | Used by |
| --- | --- | --- | --- |
| `Radius/None` | 0 | 5 | `buttonGroup`, `imageSlider`, `modal`, `selectableList` +1 · direct: `ActionMenu`, `FeedbackMessage` |
| `Radius/4` | 4 | 12 | `avatar`, `barChart`, `card`, `chartTooltip` +8 · direct: `unsafe` |
| `Radius/8` | 8 | 18 | `actionMenu`, `avatar`, `buttonGroup`, `card` +14 · direct: `ActionMenu`, `Checkbox` |
| `Radius/16` | 16 | 9 | `accordion`, `card`, `coachMark`, `feedbackMessage` +5 · direct: `CoachMark` |
| `Radius/Rounded` | 10000 | 23 | `avatar`, `badge`, `button`, `buttonGroup` +19 · direct: `DateCalendar`, `SegmentedControl` |

**All five are in use; none is orphaned** — the only token scale in the system
with full coverage, alongside Border Width.

