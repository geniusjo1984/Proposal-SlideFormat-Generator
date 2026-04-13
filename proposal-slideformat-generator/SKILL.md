---
name: proposal-slideformat-generator
description: Create consulting-style proposal slide workspaces and slide plans from user-provided RfP/RFP documents. Use when Codex needs to set up a proposal-slide project folder, create or update DESIGN.md, TASK.md, AGENT.md, or derive one-slide-per-task proposal structures from an RfP for Korean public-sector, consulting, or bid-response decks.
---

# Proposal SlideFormat Generator

Use this skill to turn an RfP into a reusable slide-production workspace, a confirmed design/task baseline, and a proposal-ready slide set.

## Quick Start

1. Initialize the workspace folders when the project structure does not exist.
2. Stop and ask the user to place the RfP and reference materials into the scaffolded folders.
3. When the user asks for a baseline design, generate `DESIGN.md` and `TASK.md`.
4. Wait for the user to review and confirm `DESIGN.md` and `TASK.md`.
5. After confirmation, generate `AGENT.md` if needed and start slide creation.
6. Revise or regenerate slides based on user review.

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
- Use `references/design-template.md` as the default design baseline only after user confirmation when `02.Reference_Templete` has no usable design reference.
- Use `references/task-template.md` when deriving `TASK.md` from a user-provided RfP.
- Use `references/agent-template.md` after the user confirms `DESIGN.md` and `TASK.md`.

## Generate DESIGN.md

When the user asks for baseline design generation:

1. Confirm that `01.Input_RfP` contains the actual RfP.
2. Inspect `02.Reference_Templete`.
3. If `02.Reference_Templete` contains template references, reconstruct `DESIGN.md` from those files while preserving the fixed baseline constraints:
   - A4 landscape
   - white background
   - consulting-style structure
   - the established blue-family palette unless the references justify a tighter adaptation
4. If `02.Reference_Templete` is empty or unusable, ask the user whether to use the default baseline from `references/design-template.md`.
5. Do not assume approval to use the default baseline until the user confirms.

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
3. Only then proceed to `AGENT.md` generation and slide creation.

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

1. Generate or update `AGENT.md` from the confirmed `DESIGN.md` and `TASK.md`.
2. Create the overall proposal logic and section map.
3. Draft one main slide per task.
4. Carry all required sub-bullets from the RfP into the slide body.
5. Refine wording into concise, proposal-style statements.
6. Check layout density and export safety for PowerPoint or PDF.

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
