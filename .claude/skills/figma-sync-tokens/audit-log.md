Seeded from Confluence page 3424288925 on 2026-08-26 — this file is now the append-only local audit log; Confluence is no longer read or written by the skill.

# Figma Variables Keys Audit

## Publish keys

Keys are only used by `importVariableByKeyAsync` when authoring inside Figma. Product code has no use for them. They are collected here so the category pages/registry stay readable.

A key survives a **rename** but not a delete-and-recreate. After either, re-read them and prove one with a round-trip before trusting the set.

## Known gaps

| Gap | Detail |
| --- | --- |
| No Figma → code name mapping | These pages give Figma token names. The code package uses its own identifiers with dev-side adjustments, and the mapping is not documented anywhere. Do not assume a Figma name matches a CSS variable or Swift constant. |
| Code-only token families | **Motion**, **Opacity**, and **Z-Index** exist in the code design system but have no Figma variables — see their dedicated pages. **Sizing** exists in code but its purpose is unconfirmed — pending a conversation between design and dev before it's documented. |
| Breakpoint and grid partial code coverage | `Breakpoint/Width` and `Min width` have code equivalents used as media-query thresholds. `Max width`, `Height`, and `Min height` are Figma-only. Grid `Count`/`Margin`/`Gutter` have code equivalents; `Width` is Figma-only (it's a computed value code doesn't need). |
| Grid layout system unconfirmed | The grid tokens exist in both Figma and code, but no layout component or asset implements them. Usage across teams is unknown. |
