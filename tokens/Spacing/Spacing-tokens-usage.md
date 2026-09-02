Unified Spacing Guidelines (Component & Layout)


### Layer 1: Micro Spacing (Inside Elements)

Used for inline micro-arrangements within atomic components and tight groupings.

| Token | Value | Primary Usage |
| --- | --- | --- |
| `Spacing/2` | 2px | Hairline spacing, badge edge adjustments, sub-pixel alignment offsets. |
| `Spacing/4` | 4px | Inline icon-to-text spacing (compact), tag vertical padding, list item counters. |
| `Spacing/6` | 6px | Intermediate micro gaps, compact status badges, avatar group overlaps. |
| `Spacing/8` | 8px | Standard icon-to-label gap, badge horizontal padding, checkbox/radio label gap. |

---

### Layer 2: Container Internals (Building New Components)

Used when assembling custom cards, disclosure panels, sheets, or container blocks.

| Token | Value | Primary Usage |
| --- | --- | --- |
| `Spacing/12` | 12px | Compact container padding (dropdown items, tooltips, compact mobile list cells). |
| `Spacing/16` | 16px | Standard internal padding on Mobile (XS–SM); content flow gap between title and body. |
| `Spacing/20` | 20px | Generous internal padding; spacing above card action footer row. |
| `Spacing/24` | 24px | Standard internal container padding on Desktop (MD–XXXL). |

#### Padding Application Matrix for Assembled Containers

| Container Type | Mobile (XS–SM) | Desktop (MD–XXXL) |
| --- | --- | --- |
| **Listing / Product Card** | `Spacing/16` | `Spacing/24` |
| **Dropdown / Popover Panel** | `Spacing/12` | `Spacing/16` |
| **Modal / Dialog Body** | `Spacing/16` | `Spacing/24` to `Spacing/32` |
| **Embedded Filter Box** | `Spacing/16` | `Spacing/16` |

---

### Layer 3: Layout Composition (Between Components)

Used for auto-layout gaps, flex gaps, and structural column offsets between sibling components.

| Token | Value | Primary Usage |
| --- | --- | --- |
| `Spacing/16` | 16px | Vertical gap between consecutive form fields; gap between inline filter chips. |
| `Spacing/24` | 24px | Standard grid gutter; horizontal & vertical gap between cards in search results. |
| `Spacing/32` | 32px | Separation between distinct card clusters; structural gap between sidebar and main rail. |
| `Spacing/40` | 40px | Extended separation between independent form sections or preview panels. |

---

### Layer 4: Page Rhythm & Viewport Margins (Macro Layout)

Used for major section separation, hero banners, and outer canvas margins.

| Token | Value | Primary Usage |
| --- | --- | --- |
| `Spacing/48` | 48px | Vertical section rhythm on Mobile/Tablet (XS–LG) between major content sections. |
| `Spacing/64` | 64px | Vertical section rhythm on Desktop (XL–XXXL) between major page sections. |
| `Spacing/80` | 80px | Hero section breathing room; outer horizontal viewport margin for XL+ tiers. |
| `Spacing/128` | 128px | Extended hero banner offsets; editorial landing section buffers on desktop. |
| `Spacing/256` | 256px | Display marketing transitions (used selectively for high-impact landing canvases). |

---

## 3. Viewport & Grid Alignment Rules

Outer page containers must strictly bind their horizontal margins and column gutters to the Breakpoint & Grid token specifications:

```text
XS (360–599px)       : Margin = 16px (Spacing/16) | Gutter = 16px (Spacing/16)
SM to LG (600–1279px): Margin = 32px (Spacing/32) | Gutter = 16px (Spacing/16)
XL+ (1280px+)        : Margin = 80px (Spacing/80) | Gutter = 24px (Spacing/24)

```

### Page Rhythm Progression Table

| Viewport Tier | Outer Margin | Section Gap | Card Grid Gap | Form Field Gap |
| --- | --- | --- | --- | --- |
| **XS / Mobile** | `Spacing/16` | `Spacing/48` | `Spacing/16` | `Spacing/16` |
| **SM / Tablet Port.** | `Spacing/32` | `Spacing/48` | `Spacing/16` | `Spacing/16` |
| **MD–LG / Tablet Land.** | `Spacing/32` | `Spacing/48` | `Spacing/24` | `Spacing/16` |
| **XL–XXXL / Desktop** | `Spacing/80` | `Spacing/64` | `Spacing/24` | `Spacing/16` |

---

## 4. AI Decision Tree for Spacing Selection

When generating or editing any UI container, evaluate the spacing level using this step-by-step logic:

```text
[ EVALUATE CONTEXT ]
         │
         ├─ Is it inside a component between icon/text/badge?
         │    └──> USE LAYER 1: Spacing/4 or Spacing/8
         │
         ├─ Is it padding or inner vertical flow for a container/card?
         │    ├── Pre-built DS component? -> Hands off (use default internal padding)
         │    └── Assembled Box/Card?     -> USE LAYER 2: Spacing/16 (mobile) or Spacing/24 (desktop)
         │
         ├─ Is it distance between sibling cards, fields, or columns?
         │    ├── Form fields stack       -> USE LAYER 3: Spacing/16
         │    ├── Card grid / row gap     -> USE LAYER 3: Spacing/24
         │    └── Sidebar to main content -> USE LAYER 3: Spacing/32
         │
         └─ Is it vertical separation between major page sections?
              ├── Mobile (XS–LG)          -> USE LAYER 4: Spacing/48
              ├── Desktop (XL+)           -> USE LAYER 4: Spacing/64
              └── Hero / Marketing block  -> USE LAYER 4: Spacing/80

```

---

## 5. Negative Scenarios ("What NOT to Do")

* ❌ **Do not hardcode pixel literals:** Never write `margin="15px"`, `gap="10px"`, or `padding="22px"`. Every spacing value must resolve to an official `Spacing/*` token.
* ❌ **Do not invert containment:** Never place a `Spacing/24` gap between inner elements inside a card that has `Spacing/16` padding.
* ❌ **Do not apply macro tokens internally:** Never use `Spacing/48` or `Spacing/64` inside individual components or cards.
* ❌ **Do not override pre-built component internals:** Never inject custom padding into `<Accordion>`, `<Button>`, or `<DatePicker>` via CSS overrides.