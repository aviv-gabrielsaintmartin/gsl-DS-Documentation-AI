*iOS and Android platform colours only. Never use in web product UI.*

## Semantic usage

| Token | When to use | Don't use for |
| --- | --- | --- |
| `Native/Android/Ripple` | Android Material ripple effect on a light/default background — touch feedback overlay | iOS or web interactions; general transparent fills (→ `Surface/Transparent`) |
| `Native/Android/Ripple-Inverted` | Android Material ripple effect on a dark/inverted background | Light-background ripples (→ `Ripple`) |
| `Native/Mobile/Background/Splashscreen` | App splash screen background on iOS and Android — set once at the OS layer, not in product screens | Any in-app screen background (→ Background family) |

## Tokens

| Token | Light | Dark | Notes |
| --- | --- | --- | --- |
| `Color/Native/Android/Ripple` | `#0000001a` | `#F8F8FA1a` | |
| `Color/Native/Android/Ripple-Inverted` | `#FFFFFF1a` | `#15171E1a` | |
| `Color/Native/Mobile/Background/Splashscreen` | `#B32730` | `#B32730` | |
