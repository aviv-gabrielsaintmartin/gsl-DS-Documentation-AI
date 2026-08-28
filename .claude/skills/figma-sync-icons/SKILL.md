---
name: figma-sync-icons
description: Extract the flat icon inventory (name, key, node ID, category, variant properties) from the GSL Foundations Figma library's "Icons" page into the local icons registry. Triggers on requests to update/sync/refresh Figma icons, or to look up/add/audit a specific icon.
metadata:
  author: Aviv
  version: "1.0.0"
  status: production
---

# Figma Icons Sync

Foundations' "Icons" page holds ~455 icons across 17 named category frames — each icon is a standalone `COMPONENT_SET` (not composed from other components, unlike Components/Patterns/Experiences). No Pattern 1/2 classification applies here: icons are leaf-level, so `figma-sync-component-sets` explicitly excludes this content and this skill owns it instead. `figma-icons-registry.json` (repo root) is the sole source of truth — Confluence is never read or written, matching the other Foundations-adjacent skills.

## Objective

Keep `figma-icons-registry.json` in sync with the live "Icons" page: one entry per icon, grouped by its category frame, capturing identity (key, node ID) and its own variant properties (not a composed Pattern 2 structure).

## Prerequisites & Mappings

| Item | Value / Configuration |
|---|---|
| **App & Plugin** | Figma Desktop with `0. GSL Foundations Library` open. Plugin: `Plugins → Development → Figma Desktop Bridge → Run` (keep active). |
| **Foundations Key** | Read from `figma-libraries-registry.json` under `foundations`. |
| **Registry** | `figma-icons-registry.json` (repo root), shaped `{"fileKey", "fileName", "page": "Icons", "categories": {"<Category Name>": {"icons": [{"name","key","nodeId","variantCount","properties"}]}}}`. |
| **Categories (17, live as of 2026-08-27)** | Action & Settings, Alert & Feedback, Brands, Navigation & Menu, Users & People, Map, Transportation, Device & Communication, Editor, Document & Content, Finance, Nature & Food, Lifestyle, Furnitures, Place & Property, Real Estate, Home. |
| **Excluded frame** | `Placeholders` — holds 2 generic template components (`placeholder`, `Figma component`), not real product icons. Never register. |
| **Audit log / Known traps** | `audit-log.md` / `known-traps.md` (this folder). |

## Steps

**STEP 0: Scope selection**
1. Check whether a specific icon or category was named. If not, and the request is a full sync, proceed against all 17 categories.
2. If an icon/category name was given, resolve to its category frame first.

**STEP 1: Registry pre-check (create vs. update)**
1. Look up the icon (by category + name) in `figma-icons-registry.json`.
2. If present: UPDATE mode — preserve any manually-added notes on that entry. If absent: CREATE mode.

**STEP 2: Extract live Figma nodes**
1. Verify Desktop Bridge is active and connected to `0. GSL Foundations Library` (`figma_get_status`, `probe: true`) — use `fileKey` targeting if it's open but not the active window, no need to switch the owner's focus.
2. `await figma.loadAllPagesAsync()`, find the page named `Icons`, then the target category frame(s) by name, excluding `Placeholders`.
3. For each icon `COMPONENT_SET` in scope, extract via `figma_execute`:
   - `name`, `key`, node ID (`id`).
   - `variantCount` (`children.length`).
   - `properties`: the full `componentPropertyDefinitions` object, preserving exact string literals — including typos/casing inconsistencies (see `known-traps.md`, e.g. a lowercase `filled` prop on some icons vs the standard `Filled`).
4. Do not walk `isExposedInstance` or classify Pattern 1/2 — icons are leaf components, this skill doesn't track composition.

**STEP 3: Diff, cache guard & anomaly detection**
1. If UPDATE mode: compare live properties against the existing registry entry.
   - **Deletion guard**: before reporting an icon as removed, force `await figma.loadAllPagesAsync()`, re-query, and verify twice (same convention as `figma-sync-component-sets`).
2. Flag, don't silently resolve:
   - A new icon name matching one already registered **in the same category** with a different key (duplicate name within a category — see `known-traps.md`'s `water-ladder` case).
   - A new/changed prop shape outside the common `{Name, Filled}` pattern (e.g. `Circle`/`Square`/`Half`/`Triangle` shape variants, a `Platform` prop) — these are legitimate, just note them; only escalate if the shape looks like a mistake.
3. If CREATE mode: build the full entry from scratch.

**STEP 4: Write the registry**
Merge the entry into `figma-icons-registry.json` under its category, preserving every other category and its manually-added notes untouched.

**STEP 5: Log & self-enrich**
1. Append a 1-2 sentence entry to `audit-log.md`.
2. If a new reproducible API/plugin trap is discovered, append a row to `known-traps.md` — never edit an existing row's meaning, only add.

**STEP 6: Report**
Print a 2-sentence confirmation: mode (CREATE/UPDATE), category, count of icons touched, registry write confirmation, whether a new trap was logged.

## Known Traps & Resolutions

See `known-traps.md` in this folder.
