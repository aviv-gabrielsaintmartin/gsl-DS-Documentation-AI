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

### Every new session
- Check the current git branch (`git branch --show-current`) before starting any task.
- Confirm with Gabriel that it's the right branch for what he's about to ask — if it looks like a different or already-merged task's branch, flag it and ask before proceeding.

### Every request
- Rephrase the request first to confirm shared understanding.
- Ask clarifying questions if relevant.
- Wait for explicit approval before starting work.
- Push back on a proposal when warranted — but always offer an alternative.
- One task = one branch. Finish it (commit, push, PR, merge) before starting the next one, rather than stacking work on top of an unrelated branch.
- Always pause for explicit go-ahead before pushing, opening a PR, or merging — never chain these automatically after a commit, even within one task.

### Every investigation
Structure findings as:
- Current state vs. intended state.
- A visual model of what's happening.
- The 2–3 root causes.
- The decisions Gabriel needs to make.

### Every PR
- Body has two sections: **Summary** (what changed and why) and **Verification** (what was checked to confirm the change works — e.g. "verified live via Figma Desktop Bridge", "confirmed registry JSON matches live Figma data"). This repo has no automated test suite, so "Verification" replaces the usual "Test plan".
- Title under 70 characters, imperative mood.

## Branch naming

`<category>/<kebab-case-description>`, e.g. `figma/sync-foundations-components`.

Current categories: `figma` (Figma sync skills work), `zeroheight` (zeroheight-confluence-transfer work), `docs` (CLAUDE.md or skill doc edits), `audit` (component-web-ai-docs runs). Extensible — add a new category when a branch's work doesn't fit any existing one, rather than forcing a bad fit.

## Repository structure

As of the 2026-09-02 manual reorg, top-level content lives in five plain-English folders (all renames of a prior structure — no content was lost; verify with `git log` if a path below seems to conflict with something older):

- `components/` — one folder per design-system component (e.g. `components/Accordion/`, `components/Button/`), each with its markdown doc and a self-contained `images/` folder.
- `tokens/` — per-category token docs (`Border width tokens.md`, `Breakpoint tokens.md`, `Motion tokens.md`, etc.), plus two categories split further into topic files: `tokens/Colors/` (`Surface.md`, `Content.md`, `Symbols.md`, `Scale.md`, `Border.md`, `Native.md`, `Color tokens.md`) and `tokens/Spacing/` (`Spacing-tokens-usage.md`, `Spacing tokens values.md`).
- `figma/` — `figma-components-registry.json`, `figma-patterns-registry.json`, `figma-experiences-registry.json`, `figma-foundations-components-registry.json`, `figma-libraries-registry.json`, `figma-tokens-registry.json`, `figma-icons-registry.json`. One per GSL library tier (Components / Patterns / Experiences / Foundations), same schema: per-entry Figma node key, `nodeId`, variant pattern classification (`Pattern 1`/`Pattern 2`), variant count, last audit date, and status (or an `assets` array in place of variant fields for a flat asset family like Brand App Icons). Sole source of truth for the `figma-sync-*` skills — Confluence is no longer read or written. The `foundations` tier covers Foundations' real components (`Flag`, `Favicon`, `Image Ratio`, `Brand Logo`, `Brand App Icons`) and — added 2026-08-28 — its 173 Illustrations, stored under a sibling top-level `illustrations` key (category-grouped, since they're catalog-sized rather than a handful of named components) — Tokens and Icons are out of this tier's scope. `figma-libraries-registry.json` maps the four GSL library tiers to their Figma library file keys (sole source of truth for `figma-sync-libraries`). `figma-tokens-registry.json` is the per-category design token inventory (sole source of truth for `figma-sync-tokens`). `figma-icons-registry.json` is the flat inventory of Foundations' "Icons" page (455 icons across 17 category frames as of 2026-08-27; sole source of truth for `figma-sync-icons`). Patterns/Experiences files are seeded empty; populate them by running the skill.
- `internal/` — internal reference docs (e.g. `GIT-BASICS-TUTORIAL.md`).
- `design-language/` — brand PDF exports (color and typography spec sheets).
- `.claude/skills/` — the six project skills described below (source of truth for their own workflows — read the `SKILL.md` files directly rather than relying on a summary).

## Skills (the "commands" of this repo)

There are no CLI build/test commands. Work happens through six Claude Code skills:

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

### `figma-sync-libraries`, `figma-sync-tokens`, `figma-sync-component-sets`, `figma-sync-icons`
Four Figma-Desktop-Bridge skills that keep the `figma-*-registry.json` files in sync with the live Figma files — Confluence is **not used** by any of them (deliberately dropped 2026-08-26: the output was only ever consumed by AI agents, never read by humans, so publishing it as Confluence pages was pure token cost with no audience). `figma-sync-component-sets` covers all node-bearing tiers (Components, Patterns, Experiences, and — added 2026-08-27 — the real components inside Foundations) with one skill rather than near-duplicates per tier — confirmed live that Patterns and Foundations' components use the identical `COMPONENT_SET`/variant/dot-prefix-private-helper structure as Components, so the extraction logic transfers as-is; it takes a tier argument (or infers it from whichever library file is open) and writes to that tier's registry file. Foundations is mixed-content: `figma-sync-component-sets` owns its real components (`Flag`, `Favicon`, `Image Ratio`, `Brand Logo`, `Brand App Icons`) and — added 2026-08-28 — its 173 Illustrations (10 categories on the "Illustrations" page, each a genuine Pattern 1/2 `COMPONENT_SET` with a `Size` variant, so this stayed in `figma-sync-component-sets` rather than becoming its own skill, unlike Icons); Foundations' Tokens stay `figma-sync-tokens`'s territory; its Icons (455 entries across 17 category frames on the "Icons" page, added 2026-08-27) got their own skill, `figma-sync-icons`, since icons are leaf components with no Pattern 1/2 composition to track — a flat name/key/category registry closer in shape to tokens than to a variant-audited component. Each skill's folder holds its own `known-traps.md` (append-only, self-enriched as new Figma/plugin quirks are found); `figma-sync-tokens` additionally caches a static `architecture.md` (brand/mode/primitive resolution model); `figma-sync-tokens`, `figma-sync-component-sets`, and `figma-sync-icons` each keep a local `audit-log.md` for run history/anomalies that used to go to a shared Confluence audit page. Full process in [`.claude/skills/figma-sync-libraries/SKILL.md`](.claude/skills/figma-sync-libraries/SKILL.md), [`.claude/skills/figma-sync-tokens/SKILL.md`](.claude/skills/figma-sync-tokens/SKILL.md), [`.claude/skills/figma-sync-component-sets/SKILL.md`](.claude/skills/figma-sync-component-sets/SKILL.md), [`.claude/skills/figma-sync-icons/SKILL.md`](.claude/skills/figma-sync-icons/SKILL.md).

## Working conventions

- Never invent Confluence page IDs, Figma keys, or Atlassian cloud IDs — read them from the registry JSON files above or resolve them live via the Atlassian/Figma MCP tools.
- The Zeroheight MCP connector is never used by any skill, even if it appears connected in a session — exports are sourced from a Confluence-staged code block or a human chat-paste fallback only.
- The four `figma-sync-*` skills never read or write Confluence — the `figma-*-registry.json` files under `figma/` are their sole source of truth.
- `figma-sync-component-sets` handles Components, Patterns, Experiences, and Foundations' real components — don't create a separate per-tier skill for a new library; extend that one instead. Foundations' Tokens (`figma-sync-tokens`) and Icons (`figma-sync-icons`) are different content shapes and stay outside this skill's scope.
- Scratch/working files (drafts, escaped HTML, verification scripts) belong in the session scratchpad directory, never committed into this repo.
