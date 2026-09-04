> **This page is evidence-based.** The **Used by** column is taken from real component bindings.

Stroke widths for borders and dividers. Values in px.

## Semantic usage

| Token | When to use |
| --- | --- |
| `Border Width/None` | No visible border — used where a filled surface stands in for an outline instead (e.g. a selected or subdued Chip). |
| `Border Width/1` | The default stroke weight for basically any bordered surface at rest — not limited to interactive controls or cards. Covers static containers and separators (Card, the optional bordered wrapper on Checkbox, plain Dividers) as much as interactive controls at rest (Text Field default border, outlined Chip, Checkbox's tick-box, Button Group items). |
| `Border Width/2` | The one narrow exception to `1` — reserved for an interactive control's active/focused state, doubling the border to signal focus independently of color. Confirmed on Text Field, where it applies at `Active` regardless of the `Error` state (error changes the border's color, not its width). |

**Open question:** a Figma link intended to show Energy tag's border (raised for a dark-mode-contrast theory) actually resolved to Checkbox instead. Energy tag renders as a flattened SVG union with no exposed border/stroke via the MCP export, so its border — if any — can't be confirmed as a `Border Width` token instance without the correct node link.

## Tokens (3)

| Token | Value | Components | Used by |
| --- | --- | --- | --- |
| `Border Width/None` | 0 | 2 | `modal`, `pagination` · direct: `Autocomplete`, `Button` |
| `Border Width/1` | 1 | 27 | `accordion`, `avatar`, `badge`, `button` +23 · direct: `Accordion`, `Checkbox` |
| `Border Width/2` | 2 | 10 | `checkbox`, `counterField`, `datePicker`, `dropdown` +6 · direct: `ActionMenu`, `Button` |

**All three are in use; none is orphaned.**
