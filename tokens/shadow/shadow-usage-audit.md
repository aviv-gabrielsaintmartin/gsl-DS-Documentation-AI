# Shadow usage audit

_Human-facing audit only — this is **not** the AI-facing ruleset. It records the live spot-check evidence behind [shadow-tokens.md](shadow-tokens.md)'s confirmed tiers, the reasoning behind the one open question that doc flags, and two anomalies that were raised and resolved rather than left open. An AI agent should read shadow-tokens.md for the rule to apply — this file exists so the evidence and reasoning don't bloat that doc._

## Method

- Spot-checked live against 8 real Figma components in the GSL Components Library: Action Menu, Coachmark, Feedback message, Snackbar, Slider, Tooltip, Modal, Bottom Sheet. A component set node (`Button`) failed to load twice and wasn't checked directly, but its "floating" variant is visible inside Action Menu.
- Page-level check against 5 real elements on the `AI reference screen` file (`bGX2uXc9TnTjpgZ1JUSPIk`): `AppClassifiedCard` (listing card), `Contact Bar` (sticky bottom CTA), `bottomBar`'s floating map/alert buttons, and small icon badges in search-suggestion rows.

## What was found

`none` and `4` hold up as confirmed tiers, matched to real components as listed in `shadow-tokens.md`. `8` and `16` are only confirmed as "this is what each named component uses" — see the open question below for why a generalizable rule couldn't be pinned down.

The page-level check reinforced the component-library findings:

- `AppClassifiedCard` and `Contact Bar` both use `none` + a border instead of a shadow, confirming `none` extends beyond banners/modals to real listing cards and sticky CTAs.
- `bottomBar`'s floating map/alert buttons carry tier `8`, confirming the floating-action-button finding from the component library.
- Small icon badges in search-suggestion rows use tier `4` as a decorative lift rather than an overlay shadow.

## Open question — `8` vs `16`

No confirmed rule distinguishes these two tiers. The floating Feedback message (`8`) and Snackbar (`16`) are both floating, temporary, similarly-sized notification-style components — nothing found in the components themselves (size, anchoring, persistence) explains why one gets less elevation than the other. A stacking-order rationale (e.g. Snackbar rendering visually above a Feedback message) is plausible but unverified — no screen was found showing both together, and no z-index documentation confirms a stacking order between them.

## Resolved anomalies (not left open)

Two apparent anomalies were raised with Gabriel and resolved, rather than flagged as open questions:

- The mobile bottom navigation bar's shadow (`0px -4px 2px rgba(0,0,0,0.04)`) doesn't match any tier — this is known Figma debt/a bug, excluded from the rules.
- The autocomplete dropdown appearing to have no shadow was only true on the mobile variant, which is a full-screen modal (already `none` per the existing modal rule) — tablet/desktop keeps the shadow, so this isn't an inconsistency.
