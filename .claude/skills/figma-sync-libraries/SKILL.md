---
name: figma-sync-libraries
description: Sync Figma library file keys (Foundations, Components, Patterns, Experiences tiers) from the active Figma Desktop file into the local registry. Triggers on requests to update/sync/refresh Figma library keys, or when a library file's key has changed and needs recording.
metadata:
  author: Aviv
  version: "2.0.0"
  status: production
---

# Figma Library Keys Sync

Local-only version of a skill formerly run against Confluence page `3423436876` ("Figma Libraries Keys", space `ADS`). Confluence is dropped entirely for this skill: the output is a machine-readable registry consumed by AI agents, not something humans read, so there was no reader-facing reason to keep publishing it there. `figma-libraries-registry.json` (repo root) is the sole source of truth.

## Objective

Keep `figma-libraries-registry.json` in sync with whichever GSL library file is currently open and focused in Figma Desktop.

## Prerequisites

| Item | Value / Configuration |
|---|---|
| **Figma Desktop** | Target library file open in Figma Desktop (the web browser app is not supported). |
| **Desktop Bridge** | Plugin active: `Plugins → Development → Figma Desktop Bridge → Run`. |
| **Registry** | `figma-libraries-registry.json` (repo root). Read and write this file directly — never Confluence. |
| **Core tiers** | `foundations`, `components`, `patterns`, `experiences` (extensible — a new tier can be added on request). |

## Steps

**STEP 1: Read the current registry**
Read `figma-libraries-registry.json` directly. This is the only source of prior state — there is no Confluence fallback to reconcile against.

**STEP 2: Inspect the active Figma file**
1. Verify the Desktop Bridge plugin is active (`figma_get_status`, `probe: true`).
2. Read the `fileKey` and document `name` of the currently focused file via `figma_execute`.

**STEP 3: Identify tier & reconcile**
1. Match the active file's name against the existing tiers.
2. If the name is new or ambiguous, ask: "Which tier does '<Active File Name>' belong to, or should I create a new tier name?"
3. Update only the target tier's `name` and `key` — leave every other entry untouched.

**STEP 4: Write the registry**
Save the updated JSON to `figma-libraries-registry.json`. There is no other output location.

**STEP 5: Report status**
Print a Markdown table of all tracked tiers (Tier, File Name, Key, Status), then end with: "Updated [<Tier Name>]. Open another library file and reply 'Next' to continue, or 'Done' to finish."

## Known Traps & Resolutions

| Trap / Behavior | Root Cause & Resolution |
|---|---|
| **Silent Bridge Disconnection** | The Desktop Bridge disconnects whenever the Figma file is edited. Re-run the plugin and verify via `figma_get_status` (`probe: true`) before retrying. |
