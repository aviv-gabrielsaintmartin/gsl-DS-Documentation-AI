<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/3403481125/Z-Index+tokens | Last modified: Aug 05, 2026 -->

# Z-Index tokens

Stacking order scale for layered UI elements. Each layer already carries a defined purpose — use the matching token rather than an arbitrary z-index value.

**Code only — no Figma equivalent** (z-index has no meaningful representation in a static design file). Token names below match the web design-system package's JSON key path exactly.

| Token | Value | Use for |
| --- | --- | --- |
| `zIndex.none` | 0 | Footer / content |
| `zIndex.1` | 20 | Tooltip / popover / dropdown |
| `zIndex.2` | 40 | Header / navigation / top bar / burger menu |
| `zIndex.3` | 60 | Overlay / backdrop / modal |
| `zIndex.4` | 80 | Toast / notification / snackbar |

_Source: web design-system package · confirmed in scope by dev team, August 2026_
