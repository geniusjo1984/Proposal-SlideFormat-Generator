---
name: proposal-slideformat-generator
description: Create consulting-style proposal slide workspaces and slide plans from user-provided RfP/RFP documents. Use when Codex needs to set up a proposal-slide project folder, create or update DESIGN.md, TASK.md, AGENT.md, or derive one-slide-per-task proposal structures from an RfP for Korean public-sector, consulting, or bid-response decks.
---

# Proposal SlideFormat Generator

Use this skill to turn an RfP into a reusable slide-production workspace and a proposal-ready task structure.

## Quick Start

1. Initialize the workspace when the project folders or control documents do not exist.
2. Read the user-provided RfP before writing any project-specific claims.
3. Create or update `DESIGN.md`, `TASK.md`, and `AGENT.md` from the templates in `references/`.
4. Plan slides from `TASK.md`, usually with one main slide per task unless the user requests another mapping.
5. Verify that every claim is traceable to the RfP or an explicit user instruction.

## Initialize The Workspace

Run the initializer when the user wants the folder structure and baseline control files created automatically.

```powershell
./scripts/init_project.ps1 -ProjectName <project-folder-name> -BasePath <parent-folder>
```

Or point directly at the full project path:

```powershell
./scripts/init_project.ps1 -ProjectRoot <target-folder>
```

The script creates these folders by default:

- `01.Input_RfP`
- `02.Reference_Templete`
- `03.Reference_Contents_Main`
- `04.Reference_Contents_Assistance`
- `05.Output_Slide`

The script also creates these files when missing:

- `DESIGN.md`
- `TASK.md`
- `AGENT.md`

Use `-IncludeOverview` to create `개요.md` only when the workspace needs an operating summary.

Use `-Force` to overwrite existing files that were previously scaffolded or intentionally replaced.

## Build The Control Documents

Use the reference files selectively instead of loading everything by default.

- Use `references/workflow.md` to understand the end-to-end operating model and folder responsibilities.
- Use `references/design-template.md` when creating or revising `DESIGN.md`.
- Use `references/task-template.md` when deriving `TASK.md` from a user-provided RfP.
- Use `references/agent-template.md` when creating the execution and quality-control rules in `AGENT.md`.
- Use `references/overview-template.md` when the workspace should include a project overview and versioning rules in `개요.md`.

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

## Draft Slides

Default to this sequence unless the user asks for a different workflow:

1. Create the overall proposal logic and section map.
2. Draft one main slide per task.
3. Carry all required sub-bullets from the RfP into the slide body.
4. Refine wording into concise, proposal-style statements.
5. Check layout density and export safety for PowerPoint or PDF.

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
