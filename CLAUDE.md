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
- `figma-components-registry.json` — per-component Figma audit tracking: Figma node key, `nodeId`, variant pattern classification (`Pattern 1`/`Pattern 2`), variant count, last audit date, and status (e.g. `Clean`, `Reclassified`).
- `figma-libraries-registry.json` — maps the four GSL library tiers (Foundations, Components, Patterns, Experiences) to their Figma library file keys.
- `figma-tokens-registry.json` — per-library design token inventory (e.g. Radius primitives), each token's name, Figma variable key, value, and the Confluence page ID documenting that token category.
- `.claude/skills/` — the two project skills described below (source of truth for their own workflows — read the `SKILL.md` files directly rather than relying on a summary).

## Skills (the "commands" of this repo)

There are no CLI build/test commands. Work happens through two Claude Code skills:

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

## Working conventions

- Never invent Confluence page IDs, Figma keys, or Atlassian cloud IDs — read them from the registry JSON files above or resolve them live via the Atlassian/Figma MCP tools.
- The Zeroheight MCP connector is never used by either skill, even if it appears connected in a session — exports are sourced from a Confluence-staged code block or a human chat-paste fallback only.
- Scratch/working files (drafts, escaped HTML, verification scripts) belong in the session scratchpad directory, never committed into this repo.
