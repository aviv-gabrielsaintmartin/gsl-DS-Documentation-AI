Stacking order for layered UI. Code-only — z-index has no meaningful
representation in a static design file.

> **This page is evidence-based.** Consumption checked against
> `gsl-core-web-design-system`.

## How stacking is actually applied

**No component token binds a z-index.** Every use is set directly in `.tsx`, and
almost all of it flows through one primitive: `Overlay`.

- `Overlay` takes a `zIndex` prop defaulting to **`zIndex.1`** — the floor for
  anything that floats.
- It publishes that value through `ZIndexContextProvider`, and **nested overlays
  sum**: an overlay opened inside another stacks above its parent automatically.
- `Modal` opts up to `zIndex.3` explicitly; `ModalWrapper` reads the context
  value rather than setting its own.

So the practical rule is: **don't set a z-index. Use `Overlay`, or a component
built on it, and let the context resolve the order.** Setting one by hand opts
out of the nesting arithmetic and is how two floating layers end up fighting.

## Tokens

| Token | Value | Intended for | Real consumers |
| --- | --- | --- | --- |
| `zIndex.none` | 0 | Footer / content | `Overlay`, `useZIndexContext` — the baseline the context counts up from |
| `zIndex.1` | 20 | Tooltip / popover / dropdown | `Overlay` (default), `Carousel`, `CoachMark` |
| `zIndex.2` | 40 | Header / navigation / top bar / burger menu | **none** |
| `zIndex.3` | 60 | Overlay / backdrop / modal | `Modal`, `DatePicker` |
| `zIndex.4` | 80 | Toast / notification / snackbar | `Notification`, `Snackbar` |

Levels `3` and `4` match their documented purpose exactly. Level `1` is the
overlay default, so its consumers are broader than "tooltip/popover".

**`zIndex.2` has no consumer.** `TopBar` — the component its description names —
sets no z-index at all and relies on document order. Either the tier is reserved
for a navigation shell that lives in product code, or it is vestigial. Flagged,
not resolved.
