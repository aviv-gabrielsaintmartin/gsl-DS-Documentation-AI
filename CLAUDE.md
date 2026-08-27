# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a source-code repository** — there is no build, lint, or test tooling here. It's a staging and reference repo for the **GSL (Gemini) Design System** documentation, used as working material for Claude Code skills that migrate/audit design-system docs into Confluence and Figma. Treat file operations here as content/data work, not software engineering: reading Zeroheight exports, matching images, and publishing to Confluence via the Atlassian MCP tools.

**Project goal**: document the design system so it's readable by AI and humans — AI is the primary audience.

**Owner**: Gabriel Saint Martin — sole owner and maintainer of this repo and its skills.

## How Claude should behave here

### Every answer
- Be concise. Short sentences.
- Use bullet points when listing elements.
- If a long answer is genuinely needed, say so and explain why before giving it.

### Every request
- Rephrase the request first to confirm shared understanding.
- Ask clarifying questions if relevant.
- Wait for explicit approval before starting work.
- Push back on a proposal when warranted — but always offer an alternative.

### Every investigation
Structure findings as:
- Current state vs. intended state.
- A visual model of what's happening.
- The 2–3 root causes.
- The decisions Gabriel needs to make.

## Repository structure

- `08 export/` — an Obsidian vault (`.obsidian/`) containing raw Zeroheight markdown exports, one file per design-system component/pattern (e.g. `Button.md`, `Accordion.md`, `Charts.md`). These are the **source content** consumed by the `zeroheight-confluence-transfer` skill.
  - `08 export/Images/` and `08 export/Images export/` — images referenced by those markdown exports.
- `Images export/` (repo root) — raw Zeroheight "Media upload" zip exports and their extracted per-component image folders (named `<hash>_<ComponentName>`, e.g. `097e03c_Button`), plus `extract_summary.csv`. These are the image assets matched by filename/hash against Confluence attachments during a transfer.
- `figma-components-registry.json`, `figma-patterns-registry.json`, `figma-experiences-registry.json`, `figma-foundations-components-registry.json` — one per GSL library tier (Components / Patterns / Experiences / Foundations), same schema: per-entry Figma node key, `nodeId`, variant pattern classification (`Pattern 1`/`Pattern 2`), variant count, last audit date, and status (or an `assets` array in place of variant fields for a flat asset family like Brand App Icons). Sole source of truth for `figma-sync-component-sets` — Confluence is no longer read or written. The `foundations` tier only covers Foundations' real components (`Flag`, `Favicon`, `Image Ratio`, `Brand Logo`, `Brand App Icons`) — Tokens and Icons are out of its scope (see below). Patterns/Experiences/Foundations files are seeded empty; populate them by running the skill.
- `figma-libraries-registry.json` — maps the four GSL library tiers (Foundations, Components, Patterns, Experiences) to their Figma library file keys. Sole source of truth for `figma-sync-libraries`.
- `figma-tokens-registry.json` — per-category design token inventory (colors, spacing, radius, border-width, breakpoints, grid, effect styles, text styles), each token's name, Figma variable key, and value. Sole source of truth for `figma-sync-tokens`.
- `.claude/skills/` — the five project skills described below (source of truth for their own workflows — read the `SKILL.md` files directly rather than relying on a summary).

## Skills (the "commands" of this repo)

There are no CLI build/test commands. Work happens through five Claude Code skills:

### `zeroheight-confluence-transfer`
Transfers one component's Zeroheight markdown export (staged in a `<pre><code class="language-markdown">` block on the target Confluence page, alongside pre-uploaded image attachments) into that page, restructured against a fixed template. Key facts:
- Master template is cached locally at `.claude/skills/zeroheight-confluence-transfer/template.html` (mirrors Confluence page `3430449284`) — read the local cache, don't fetch Confluence unless the template owner says it changed.
- Target Confluence space is `ADS`; cloud ID is `4449da05-ef5a-4725-9fc8-353497e0c212`.
- Images are matched to attachments by filename/hash correlation only — never opened or visually inspected.
- Publishing is single-pass (assemble → publish → one verification script against one read-back) — no draft-to-disk round trips.
- Batch runs (multiple components in one sitting) dispatch each component to its own isolated subagent.
- Full step-by-step process, table color conventions, and a substantial "Known Traps" table (unpaired DO/DON'T rows, wide-table splitting, orphaned "Platform" sections, etc.) live in [`.claude/skills/zeroheight-confluence-transfer/SKILL.md`](.claude/skills/zeroheight-confluence-transfer/SKILL.md) — follow it exactly rather than improvising the format.

### `component-web-ai-docs`
Given a Confluence link to a GSL component page (space `ADS`), audits the component's **real web implementation** (expected at `libraries/ui/src/{ComponentName}/` — in the separate product codebase, not this repo) against its Confluence usage doc, and publishes three new child pages: an audit/triage report, a platform-agnostic decision tree, and an LLM-ready API spec. Full process in [`.claude/skills/component-web-ai-docs/SKILL.md`](.claude/skills/component-web-ai-docs/SKILL.md). This skill must be run from (or given access to) the actual component source repo to find real code — it cannot ground findings in this documentation-only repo alone.

### `figma-sync-libraries`, `figma-sync-tokens`, `figma-sync-component-sets`
Three Figma-Desktop-Bridge skills that keep the `figma-*-registry.json` files in sync with the live Figma files — Confluence is **not used** by any of them (deliberately dropped 2026-08-26: the output was only ever consumed by AI agents, never read by humans, so publishing it as Confluence pages was pure token cost with no audience). `figma-sync-component-sets` covers all node-bearing tiers (Components, Patterns, Experiences, and — added 2026-08-27 — the real components inside Foundations) with one skill rather than near-duplicates per tier — confirmed live that Patterns and Foundations' components use the identical `COMPONENT_SET`/variant/dot-prefix-private-helper structure as Components, so the extraction logic transfers as-is; it takes a tier argument (or infers it from whichever library file is open) and writes to that tier's registry file. Foundations is mixed-content: this skill only owns its real components (`Flag`, `Favicon`, `Image Ratio`, `Brand Logo`, `Brand App Icons`); Foundations' Tokens stay `figma-sync-tokens`'s territory, and its Icons (~600+ entries on the "Icons" page) and Illustrations (100+ sets) are explicitly out of scope for all three skills as of 2026-08-27 — Icons is slated for its own future skill (a flat name/key/category registry, closer in shape to tokens than to a variant-audited component). Each skill's folder holds its own `known-traps.md` (append-only, self-enriched as new Figma/plugin quirks are found); `figma-sync-tokens` additionally caches a static `architecture.md` (brand/mode/primitive resolution model); `figma-sync-tokens` and `figma-sync-component-sets` both keep a local `audit-log.md` for run history/anomalies that used to go to a shared Confluence audit page. Full process in [`.claude/skills/figma-sync-libraries/SKILL.md`](.claude/skills/figma-sync-libraries/SKILL.md), [`.claude/skills/figma-sync-tokens/SKILL.md`](.claude/skills/figma-sync-tokens/SKILL.md), [`.claude/skills/figma-sync-component-sets/SKILL.md`](.claude/skills/figma-sync-component-sets/SKILL.md).

## Working conventions

- Never invent Confluence page IDs, Figma keys, or Atlassian cloud IDs — read them from the registry JSON files above or resolve them live via the Atlassian/Figma MCP tools.
- The Zeroheight MCP connector is never used by any skill, even if it appears connected in a session — exports are sourced from a Confluence-staged code block or a human chat-paste fallback only.
- The three `figma-sync-*` skills never read or write Confluence — the `figma-*-registry.json` files at repo root are their sole source of truth.
- `figma-sync-component-sets` handles Components, Patterns, Experiences, and Foundations' real components — don't create a separate per-tier skill for a new library; extend that one instead. Foundations' Tokens and Icons are different content shapes and stay outside this skill's scope.
- Scratch/working files (drafts, escaped HTML, verification scripts) belong in the session scratchpad directory, never committed into this repo.
