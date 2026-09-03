# Radius usage audit

_Human-facing audit only — this is **not** the AI-facing ruleset. It records the live spot-check evidence behind [radius-tokens.md](radius-tokens.md)'s confirmed rule, plus two things noticed along the way that are out of scope for the token doc itself. An AI agent should read radius-tokens.md for the rule to apply — this file exists so the evidence and tangential findings don't bloat that doc._

## Why this exists

Most components don't name a radius token in their own Confluence docs, so the size/shape-tiered rule in `radius-tokens.md` needed to be checked directly against live components and real pages rather than taken from a naming convention.

## Method

- Spot-checked live against 9 real Figma components in the GSL Components Library: Card, Text Field, Snackbar, Text Button, Accordion, Coach mark, Button, Tag, Chip.
- Page-level check against 3 real screens in the `AI reference screen` file (`bGX2uXc9TnTjpgZ1JUSPIk`): home/search, search prompt, results list.

## What was found

The size/shape-tiered rule holds across all 9 components, with one nuance: it's not purely size-based. Text Button is small but rectangular (`8`), while Button/Tag/Chip are pill regardless of size — shape category (filled/interactive control vs. rectangular container) determines the tier at least as much as size.

Page-level check confirmed the same tiers in context: card `16`, badges/tags/buttons pill `100`, provider logo badge `8`/`4` nested. No wrong-tier values found on any of the 3 screens.

Radius is applied as a hardcoded pixel literal rather than a bound token/variable in every page node checked — unlike color/typography on the same nodes. This is the same known Figma-only "Corner radius" layer gap noted below, now confirmed to extend to real pages, not just the component library.

## Notes (resolved non-issues)

- **Pill value binding:** pill components (Button, Tag, Chip) bind their own component-level value (`96`–`100`) rather than literally referencing `Radius/Rounded` (`10000`). Both clamp to the same visual capsule, so this is expected Figma behavior, not a discrepancy — confirmed non-issue per Gabriel.

## Out of scope

- Figma has an unimplemented, undocumented intermediate "Corner radius" semantic layer (per-component variables like `Corner radius/Accordion`) sitting between the `Radius/*` primitives and components. Out of scope since it isn't built in code yet.
- Separately noticed (not a radius issue): on the results-list screen, the "Newest ▾" sort control is a custom-built frame, not a real Button/Text Button instance — though its radius value happens to be correct.
