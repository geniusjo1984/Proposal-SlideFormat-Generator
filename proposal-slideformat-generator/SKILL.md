---
name: proposal-slideformat-generator
description: Create consulting-style proposal slide workspaces and slide plans from user-provided RfP/RFP documents. Use when Codex needs to set up a proposal-slide project folder, create or update DESIGN.md, TASK.md, reuse or create AGENT.md, or derive one-slide-per-task proposal structures from an RfP for Korean public-sector, consulting, or bid-response decks.
---

# Proposal SlideFormat Generator

Use this skill to turn an RfP into a reusable slide-production workspace, a confirmed design/task baseline, and a proposal-ready slide set.

Prefer Stitch-based slide generation when it is available in the user's environment.

## Quick Start

1. Initialize the workspace folders when the project structure does not exist.
2. Stop and ask the user to place the RfP and reference materials into the scaffolded folders.
3. When the user asks for a baseline design, generate `DESIGN.md` and `TASK.md`.
4. Wait for the user to review and confirm `DESIGN.md` and `TASK.md`.
5. After confirmation, reuse an existing user-provided `AGENT.md` when it exists. Generate `AGENT.md` only when it is missing or the user explicitly asks for regeneration.
6. Revise or regenerate slides based on user review.

## Preferred Execution Path

Use this execution priority for slide creation:

1. If Stitch MCP is available, use it as the preferred slide-generation path.
2. Otherwise, if a Stitch skill is available, use that workflow.
3. If Stitch is not available, first recommend that the user install Stitch.
4. If Stitch is still unavailable or the user declines, continue with the standard workflow using confirmed `DESIGN.md` and `TASK.md`.

## Initialize The Workspace

Run the initializer when the user wants the project folder structure created automatically.

```powershell
./scripts/init_project.ps1 -ProjectName <project-folder-name> -BasePath <parent-folder>
```

Or point directly at the full project path:

```powershell
./scripts/init_project.ps1 -ProjectRoot <target-folder>
```

The script creates folders only and writes reminder files that tell the user where to place the RfP and references.

The script creates these folders:

- `01.Input_RfP`
- `02.Reference_Templete`
- `03.Reference_Contents_Main`
- `04.Reference_Contents_Assistance`
- `05.Output_Slide`

Use `-Force` to overwrite existing reminder files that were previously scaffolded.

## Input Gate

Do not create `DESIGN.md`, do not create `TASK.md`, and do not draft slides until the user has placed the actual RfP and relevant references into the workspace.

If the workspace has been scaffolded but the required inputs are missing:

1. Stop after folder setup.
2. Tell the user to place the RfP in `01.Input_RfP`.
3. Tell the user to place slide-format references in `02.Reference_Templete` when available.
4. Resume only after the source files are present.

## Build The Control Documents

Use the reference files selectively instead of loading everything by default.

- Use `references/workflow.md` to understand the end-to-end operating model and folder responsibilities.
- Use `references/design-template.md` as the mandatory fallback baseline when `02.Reference_Templete` has no usable design reference.
- Use `references/task-template.md` when deriving `TASK.md` from a user-provided RfP.
- Use `references/agent-template.md` only when the workspace does not already contain a user-provided `AGENT.md` or the user explicitly asks to regenerate it.

## AGENT.md Reuse Rule

Treat a user-provided `AGENT.md` as authoritative by default.

When the workspace already contains `AGENT.md`:

1. Reuse it as-is when it is already compatible with the current workflow.
2. Do not regenerate it just because `DESIGN.md` or `TASK.md` changed.
3. Only update it when the file is missing required placeholders, contradicts the confirmed workflow, or the user explicitly asks for a rewrite.
4. If a basic baseline file is acceptable to the user, copying or lightly adapting that baseline is preferred over drafting a brand-new `AGENT.md`.

## Design Reference Boundary

When building `DESIGN.md`, the design-source boundary is strict:

1. `02.Reference_Templete` is the only workspace folder that may be inspected for visual, formatting, or layout references.
2. `03.Reference_Contents_Main` and `04.Reference_Contents_Assistance` may inform slide content, evidence, or wording, but must not be used as design-reference fallback sources.
3. Do not search sibling folders, parent folders, unrelated project files, or ad hoc local files for substitute design references.
4. If `02.Reference_Templete` is empty or unusable, immediately use `references/design-template.md`.

## Generate DESIGN.md

When the user asks for baseline design generation:

1. Confirm that `01.Input_RfP` contains the actual RfP.
2. Inspect only `02.Reference_Templete`.
3. Do not inspect `03.Reference_Contents_Main`, `04.Reference_Contents_Assistance`, sibling folders, parent folders, or unrelated files for design-reference fallback.
4. If `02.Reference_Templete` contains template references, reconstruct `DESIGN.md` from those files while preserving the fixed baseline constraints:
   - A4 landscape
   - white background
   - consulting-style structure
   - the established blue-family palette unless the references justify a tighter adaptation
5. If `02.Reference_Templete` is empty or unusable, use the default baseline from `references/design-template.md` immediately.

## Derive TASK.md From The RfP

Treat `TASK.md` as a project-specific output, not a fixed asset.

When building `TASK.md`:

1. Extract the governing section hierarchy from the RfP.
2. Preserve the original task granularity unless the user explicitly wants consolidation.
3. Record task-specific source bullets that must not be dropped.
4. Draft a message-driven slide title and one-line lead message for each task.
5. Assign the clearest slide form for each task, such as a table, process, matrix, framework, roadmap, or stakeholder map.
6. Keep terminology consistent with the RfP and the user's proposal style.

If the RfP is ambiguous, keep the structure generic rather than inventing unsupported detail.

## Review Gate

After generating `DESIGN.md` and `TASK.md`:

1. Stop for user review.
2. Revise those files until the user confirms them.
3. Only then proceed to `AGENT.md` reuse or generation and slide creation.

## Fixed Design Baseline

Treat the design baseline from `references/design-template.md` as mandatory by default:

- A4 landscape is mandatory
- White background only
- Use the fixed blue-family palette
- Use message-driven titles
- Use structured consulting layouts rather than paragraph-heavy pages
- Do not fall back to 16:9 unless the user explicitly changes the requirement

## Draft Slides

Default to this sequence unless the user asks for a different workflow:

1. Reuse the existing `AGENT.md` when the user has provided one. Generate or update `AGENT.md` only when it is missing or the user explicitly asks for a new project-specific version.
2. Check whether Stitch MCP or a Stitch skill is available.
3. If Stitch is unavailable, recommend installation before proceeding.
4. Create the overall proposal logic and section map.
5. Draft one main slide per task.
6. Carry all required sub-bullets from the RfP into the slide body.
7. Refine wording into concise, proposal-style statements.
8. Check layout density and export safety for PowerPoint or PDF.

## Quality Control

Before finalizing any slide plan or deck:

- Confirm that every slide maps back to a task in `TASK.md`.
- Confirm that every nontrivial claim is supported by the RfP or explicit user input.
- Confirm that no required sub-item from the source structure was dropped.
- Confirm that titles are lead messages rather than noun-only labels.
- Confirm that the design guidance in `DESIGN.md` is internally consistent.
- Confirm that tables and diagrams remain readable at the target slide size.

## Notes

Keep `SKILL.md` lean. Put project-specific detail into the workspace documents and keep reusable logic in `references/` and `scripts/`.
