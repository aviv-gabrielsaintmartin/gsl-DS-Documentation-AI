> **This page is evidence-based.** The **Used by** column lists the components
> that actually bind each token in `gsl-core-web-design-system`, generated from
> [color/color-usage-ledger.md](color-usage-ledger.md). **not used** means no
> component binds it — do not reach for it.
> Rules for generating UI: [color-rules-ai.md](color-rules-ai.md).
> Evidence and verdicts: [color-usage-audit.md](color-usage-audit.md).

Page-level backgrounds. *`Background` is the page/screen canvas — for component fills (cards, buttons, inputs, sheets) use `Surface` instead.*

## Semantic usage

| Token | When to use | Don't use for | Used by |
| --- | --- | --- | --- |
| `Background/Default` | The base page/screen canvas behind all content. Applied once by the theme provider, not per-component. ⚠️ `#FFFFFF` in light — the same as nine other tokens; pick it by role, never because you need white. | Component fills (→ `Surface/Default`) | direct: `GeminiProvider` |
| `Background/Light` | **Not used.** No production consumer — it appears only in a Storybook story. | Section separation (→ `Background/Subdued`, which is used) | **not used** |
| `Background/Subdued` | A more recessed page-level background — e.g. behind a scrollable region or muted section. Also the `skeleton` shimmer gradient. | Disabled component states (→ `Surface/Disabled`) | `skeleton` · direct: `ImageSlider` |
| `Background/Backdrop/Default` | The scrim behind modals, bottom sheets, popups | Any in-flow (non-overlay) UI | `backdrop` |
| `Background/Constant/Black` | **Not used.** For an immersive media backdrop, `Surface/Constant/Black` has consumers (`imageSlider`, `tag`). | Anything that should respond to theme | **not used** |
| `Background/Constant/White` | **Not used.** | Anything that should respond to theme | **not used** |

## Tokens

| Token | Light | Dark |
| --- | --- | --- |
| `Color/Background/Backdrop/Default` | `#0000004d` | `#15171E99` |
| `Color/Background/Constant/Black` | `#000000` | `#000000` |
| `Color/Background/Constant/White` | `#FFFFFF` | `#FFFFFF` |
| `Color/Background/Default` | `#FFFFFF` | `#15171E` |
| `Color/Background/Light` | `#F9F9F9` | `#292D3B` |
| `Color/Background/Subdued` | `#EEEEEE` | `#3D4459` |
