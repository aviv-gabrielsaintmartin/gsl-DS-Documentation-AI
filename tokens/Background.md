Page-level backgrounds. *`Background` is the page/screen canvas — for component fills (cards, buttons, inputs, sheets) use `Surface` instead.*

## Semantic usage

| Token | When to use | Don't use for |
| --- | --- | --- |
| `Background/Default` | The base page/screen canvas behind all content | Component fills (→ Surface) |
| `Background/Light` | Alternate page-level background for a section needing subtle separation from Default | Card/component backgrounds (→ `Surface/Light`) |
| `Background/Subdued` | A more recessed page-level background — e.g. behind a scrollable region or muted section | Disabled component states (→ `Surface/Disabled`) |
| `Background/Backdrop/Default` | The scrim behind modals, bottom sheets, popups | Any in-flow (non-overlay) UI |
| `Background/Constant/Black` | Fixed black background, ignores brand and light/dark mode — immersive media, video | Anything that should respond to theme |
| `Background/Constant/White` | Fixed white background, ignores brand and light/dark mode | Anything that should respond to theme |

## Tokens

| Token | Light | Dark |
| --- | --- | --- |
| `Color/Background/Backdrop/Default` | `#0000004d` | `#15171E99` |
| `Color/Background/Constant/Black` | `#000000` | `#000000` |
| `Color/Background/Constant/White` | `#FFFFFF` | `#FFFFFF` |
| `Color/Background/Default` | `#FFFFFF` | `#15171E` |
| `Color/Background/Light` | `#F9F9F9` | `#292D3B` |
| `Color/Background/Subdued` | `#EEEEEE` | `#3D4459` |
