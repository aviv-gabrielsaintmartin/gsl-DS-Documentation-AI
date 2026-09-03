# Surface × Border combination audit

_Human-facing audit only — this is **not** the AI-facing ruleset. It records every combination tested, including the ones that fail, so nothing gets silently lost. The AI agent should only ever be pointed to a separate, filtered "allowed combinations" file containing the ✅ survivors — never this one, to avoid a probabilistic agent picking an accessible-but-design-wrong pair from a table that also contains failures._

## Why this exists

`Status`, `Score`, and `Decorative` families already have an obvious 1:1 domain pairing documented in their own "when to use" text (e.g. `Surface/Status/Error` pairs with `Border/Status/Error`) — no real ambiguity there. `Constant` is excluded here entirely: it follows a separate categorical rule (`Surface/Constant/*` may only pair with `Border/Constant/*` or `Content/Constant/*`, never a re-themeable base token, since Constant must stay fixed across light/dark mode) — that gets its own audit, not yet run. What's left — the **base/neutral cluster** — is the genuinely open case: no naming convention states which pairings are safe, so it needs to be checked directly.

## Scope

- **Mode**: Light only. Dark mode is a separate, deferred audit.
- **Surfaces**: Default state only (`Default`, `Light`, `Subdued`, `Disabled`, `Dark`, `Accent/Light`, `Active`, `Interactive/Selected`). Included here because none of them have an explicit naming-based pairing rule like the `On-X` tokens — not because they're all neutral. `Accent/Light` and `Active` are in fact brand-tinted (a pale red for SeLoger, a different hue per brand), not neutral; they're grouped with the others purely because the ambiguity (which border goes with them) is the same. Excludes `Transparent` variants (alpha-compositing, different mechanism) and `Default/Inverted` (already pinned by naming — pairs with `Content/Default/Inverted`/inverted contexts by definition).
- **Borders**: `Interactive` and `Active` get their Hover/Pressed states included too, since border visibility disappearing on hover/click was the specific concern that prompted this audit. All other border families are Default-state only.
- **Threshold**: WCAG 1.4.11 non-text contrast, ≥3:1 — a border's job is visibility, not legibility, so the lower (vs. 4.5:1 text) threshold applies.
- **Method**: ratios computed by hand from the WCAG relative-luminance formula, using the hex values already documented in [Surface.md](Surface.md) and [Border.md](Border.md). High confidence away from the boundary; entries within ~2.8–3.2:1 (marked below) are worth re-checking with an actual contrast-checker tool before being treated as final.

**Legend**: ✅ passes · ❌ fails · 🔲 identical hex — literally invisible, not just low-contrast · ⚠️ passes with a thin margin.

## Candidates for review

These are **candidates flagged by the math, not confirmed defects.** Token-level contrast checking can only tell you two hex values are identical or too close — it can't tell you whether that was intentional. It's already known that at least one identical-hex case in this space is a deliberate design decision (a button-group's selected state was given a surface/border matching color on purpose, to fix a different visual bug — a false 1px inset illusion where a lighter border against a darker surface made the edge look height-reduced). Some components also have no border at all in their default state, gaining one only via `Interactive` on hover/press — so "no visible border here" can be correct by design, not a gap. Each item below needs a design call, not an automatic exclusion — see "Not yet audited" for how to resolve the ones you're unsure about.

Five pairs resolve to the **exact same hex value** in Light mode, making the border completely invisible:

- `Border/Surface` on `Surface/Subdued` (`#EEEEEE` on `#EEEEEE`)
- `Border/Light` / `Border/Disabled` on `Surface/Disabled` (`#E0E0E0` on `#E0E0E0`)
- `Border/Subdued` on `Surface/Dark` (`#959595` on `#959595`)
- `Border/Accent/Light` on `Surface/Accent/Light` / `Surface/Active` (`#FCE6E7` on `#FCE6E7`)
- `Border/Interactive/Default` on `Surface/Interactive/Selected` (`#4B4B4B` on `#4B4B4B`)

One matched state-transition pair fails outright: `Surface/Active/Pressed` + `Border/Active/Pressed` = **2.89:1**, below the 3:1 floor. This is the exact combination a component would use on click for this family — a concrete, token-level candidate matching the "border disappears on click" pattern reported separately, though confirming a live component actually deploys this pair still requires checking the real component code (out of scope for this markdown-only audit).

Two structural gaps exist with no token to test against:
- `Border/Active` has no `Hover` state at all — only `Default`/`Pressed` — so a component using this family on hover has nothing dedicated to transition to.
- No `Border/Selected` family exists anywhere, so `Surface/Interactive/Selected` has no matching border token in any state.

## Static pairing matrix (Default state)

### `Surface/Default/Default` `#FFFFFF`

| Border                                 | Ratio   | Verdict     |
| -------------------------------------- | ------- | ----------- |
| `Border/Interactive/Pressed` `#000000` | 21.0:1  | ✅           |
| `Border/Interactive/Hover` `#323232`   | 12.84:1 | ✅           |
| `Border/Default` `#323232`             | 12.84:1 | ✅           |
| `Border/Interactive/Default` `#4B4B4B` | 8.72:1  | ✅           |
| `Border/Active/Pressed` `#C10410`      | 6.38:1  | ✅           |
| `Border/Focus` `#C10410`               | 6.38:1  | ✅           |
| `Border/Active/Default` `#E30513`      | 4.89:1  | ✅           |
| `Border/Subdued` `#959595`             | 2.99:1  | ❌ near miss |
| `Border/Light` `#E0E0E0`               | 1.32:1  | ❌           |
| `Border/Disabled` `#E0E0E0`            | 1.32:1  | ❌           |
| `Border/Accent/Light` `#FCE6E7`        | 1.19:1  | ❌           |
| `Border/Surface` `#EEEEEE`             | 1.16:1  | ❌           |

### `Surface/Light/Default` `#F9F9F9`

| Border                                 | Ratio   | Verdict |
| -------------------------------------- | ------- | ------- |
| `Border/Interactive/Pressed` `#000000` | 19.95:1 | ✅       |
| `Border/Interactive/Hover` `#323232`   | 12.19:1 | ✅       |
| `Border/Default` `#323232`             | 12.19:1 | ✅       |
| `Border/Interactive/Default` `#4B4B4B` | 8.28:1  | ✅       |
| `Border/Active/Pressed` `#C10410`      | 6.06:1  | ✅       |
| `Border/Focus` `#C10410`               | 6.06:1  | ✅       |
| `Border/Active/Default` `#E30513`      | 4.64:1  | ✅       |
| `Border/Subdued` `#959595`             | 2.84:1  | ❌       |
| `Border/Light` `#E0E0E0`               | 1.25:1  | ❌       |
| `Border/Disabled` `#E0E0E0`            | 1.25:1  | ❌       |
| `Border/Surface` `#EEEEEE`             | 1.10:1  | ❌       |
| `Border/Accent/Light` `#FCE6E7`        | 1.13:1  | ❌       |

### `Surface/Subdued/Default` `#EEEEEE`

| Border | Ratio | Verdict |
|---|---|---|
| `Border/Interactive/Pressed` `#000000` | 18.10:1 | ✅ |
| `Border/Interactive/Hover` `#323232` | 11.06:1 | ✅ |
| `Border/Default` `#323232` | 11.06:1 | ✅ |
| `Border/Interactive/Default` `#4B4B4B` | 7.51:1 | ✅ |
| `Border/Active/Pressed` `#C10410` | 5.50:1 | ✅ |
| `Border/Focus` `#C10410` | 5.50:1 | ✅ |
| `Border/Active/Default` `#E30513` | 4.21:1 | ✅ |
| `Border/Subdued` `#959595` | 2.58:1 | ❌ |
| `Border/Light` `#E0E0E0` | 1.14:1 | ❌ |
| `Border/Disabled` `#E0E0E0` | 1.14:1 | ❌ |
| `Border/Accent/Light` `#FCE6E7` | 1.03:1 | ❌ |
| `Border/Surface` `#EEEEEE` | 1.00:1 | 🔲 identical |

### `Surface/Disabled` `#E0E0E0`

| Border | Ratio | Verdict |
|---|---|---|
| `Border/Interactive/Pressed` `#000000` | 15.90:1 | ✅ |
| `Border/Interactive/Hover` `#323232` | 9.72:1 | ✅ |
| `Border/Default` `#323232` | 9.72:1 | ✅ |
| `Border/Interactive/Default` `#4B4B4B` | 6.60:1 | ✅ |
| `Border/Active/Pressed` `#C10410` | 4.83:1 | ✅ |
| `Border/Focus` `#C10410` | 4.83:1 | ✅ |
| `Border/Active/Default` `#E30513` | 3.70:1 | ✅ |
| `Border/Subdued` `#959595` | 2.27:1 | ❌ |
| `Border/Surface` `#EEEEEE` | 1.14:1 | ❌ |
| `Border/Accent/Light` `#FCE6E7` | 1.11:1 | ❌ |
| `Border/Light` `#E0E0E0` | 1.00:1 | 🔲 identical |
| `Border/Disabled` `#E0E0E0` | 1.00:1 | 🔲 identical |

### `Surface/Dark/Default` `#959595`

| Border | Ratio | Verdict |
|---|---|---|
| `Border/Interactive/Pressed` `#000000` | 7.01:1 | ✅ |
| `Border/Interactive/Hover` `#323232` | 4.29:1 | ✅ |
| `Border/Default` `#323232` | 4.29:1 | ✅ |
| `Border/Interactive/Default` `#4B4B4B` | 2.91:1 | ❌ near miss |
| `Border/Surface` `#EEEEEE` | 2.58:1 | ❌ |
| `Border/Accent/Light` `#FCE6E7` | 2.51:1 | ❌ |
| `Border/Light` `#E0E0E0` | 2.27:1 | ❌ |
| `Border/Disabled` `#E0E0E0` | 2.27:1 | ❌ |
| `Border/Active/Pressed` `#C10410` | 2.13:1 | ❌ |
| `Border/Focus` `#C10410` | 2.13:1 | ❌ |
| `Border/Active/Default` `#E30513` | 1.63:1 | ❌ |
| `Border/Subdued` `#959595` | 1.00:1 | 🔲 identical |

### `Surface/Accent/Light/Default` `#FCE6E7`

| Border | Ratio | Verdict |
|---|---|---|
| `Border/Interactive/Pressed` `#000000` | 17.61:1 | ✅ |
| `Border/Interactive/Hover` `#323232` | 10.77:1 | ✅ |
| `Border/Default` `#323232` | 10.77:1 | ✅ |
| `Border/Interactive/Default` `#4B4B4B` | 7.32:1 | ✅ |
| `Border/Active/Pressed` `#C10410` | 5.35:1 | ✅ |
| `Border/Focus` `#C10410` | 5.35:1 | ✅ |
| `Border/Active/Default` `#E30513` | 4.10:1 | ✅ |
| `Border/Subdued` `#959595` | 2.51:1 | ❌ |
| `Border/Light` `#E0E0E0` | 1.11:1 | ❌ |
| `Border/Disabled` `#E0E0E0` | 1.11:1 | ❌ |
| `Border/Surface` `#EEEEEE` | 1.03:1 | ❌ |
| `Border/Accent/Light` `#FCE6E7` | 1.00:1 | 🔲 identical |

### `Surface/Active/Default` `#FCE6E7`

_Identical hex to `Surface/Accent/Light` above — same results apply._

### `Surface/Interactive/Selected/Default` `#4B4B4B`

| Border                                 | Ratio  | Verdict      |
| -------------------------------------- | ------ | ------------ |
| `Border/Surface` `#EEEEEE`             | 7.51:1 | ✅            |
| `Border/Accent/Light` `#FCE6E7`        | 7.32:1 | ✅            |
| `Border/Light` `#E0E0E0`               | 6.60:1 | ✅            |
| `Border/Disabled` `#E0E0E0`            | 6.60:1 | ✅            |
| `Border/Subdued` `#959595`             | 2.91:1 | ❌ near miss  |
| `Border/Interactive/Pressed` `#000000` | 2.41:1 | ❌            |
| `Border/Active/Default` `#E30513`      | 1.79:1 | ❌            |
| `Border/Interactive/Hover` `#323232`   | 1.47:1 | ❌            |
| `Border/Default` `#323232`             | 1.47:1 | ❌            |
| `Border/Active/Pressed` `#C10410`      | 1.37:1 | ❌            |
| `Border/Focus` `#C10410`               | 1.37:1 | ❌            |
| `Border/Interactive/Default` `#4B4B4B` | 1.00:1 | 🔲 identical |

## Matched state-transition checks

_Static pairing only tells you if a resting composition works. These check whether a family's surface and border stay compatible when both transition together on hover/press — the case most relevant to a border disappearing on interaction._

### Interactive — matched state transitions

| State | Surface | Border | Ratio | Verdict |
|---|---|---|---|---|
| Hover | `Surface/Interactive/Hover` `#E0E0E0` | `Border/Interactive/Hover` `#323232` | 9.72:1 | ✅ |
| Pressed | `Surface/Interactive/Pressed` `#AEAEAE` | `Border/Interactive/Pressed` `#000000` | 9.46:1 | ✅ |

### Active — matched state transitions

| State | Surface | Border | Ratio | Verdict |
|---|---|---|---|---|
| Hover | `Surface/Active/Hover` `#F8C3C6` | `Border/Active/Default` `#E30513` _(reused — no dedicated Hover border)_ | 3.17:1 | ⚠️ thin margin |
| Pressed | `Surface/Active/Pressed` `#F3949A` | `Border/Active/Pressed` `#C10410` | 2.89:1 | ❌ |

## Not yet audited

- **Design-intent annotation of the flagged candidates above** — before any of these get excluded from the AI-facing authorized-combinations list, each one needs a call: intentional (like the button-group case), a genuine gap worth fixing later, or unknown. For unknowns, escalate to a targeted check against the real component/Figma rather than guessing from token math alone.
- `Constant` cluster (`Surface/Constant/*` × `Border/Constant/*`) — separate categorical rule, no contrast math run yet.
- `Surface` × `Content` combination matrix — same method, not started.
- Dark mode — deferred entirely, separate batch.
- Any pairing's real usage in a live component — this file only checks token math, not what a component actually implements. That check needs the component's real source, outside this repo.
