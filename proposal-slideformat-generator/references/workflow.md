# Proposal Slide Workflow

## Purpose

Use this workflow to set up and run a repeatable RfP-based proposal-slide project.

## Default Folder Structure

- `01.Input_RfP`: Store the primary RfP or source request documents.
- `02.Reference_Templete`: Store template decks, example slides, or formatting references.
- `03.Reference_Contents_Main`: Store primary supporting references used to build the proposal logic.
- `04.Reference_Contents_Assistance`: Store secondary references, supplemental cases, or detailed evidence.
- `05.Output_Slide`: Store working slide drafts and final outputs.

## Operating Sequence

1. Install the skill.
2. Scaffold the project folders.
3. Ask the user to place the RfP and supporting references into the folders.
4. When the user requests baseline design, generate `DESIGN.md` and `TASK.md`.
5. For `DESIGN.md`, inspect `02.Reference_Templete` first.
6. If `02.Reference_Templete` has usable references, reconstruct `DESIGN.md` from those references while preserving the fixed A4-landscape baseline.
7. If `02.Reference_Templete` is empty, ask the user to confirm use of the default baseline from `references/design-template.md`.
8. Stop for user review and confirmation of `DESIGN.md` and `TASK.md`.
9. After confirmation, create `AGENT.md` and draft slides in `05.Output_Slide`.
10. Revise or regenerate slides based on user feedback.

## Document Roles

- `DESIGN.md`: Fixed design authority for A4 landscape layout, color system, typography, spacing, and wording style. Rebuild it from `02.Reference_Templete` when template references exist.
- `TASK.md`: Project-specific source of truth for slide planning.
- `AGENT.md`: Execution rules for reading order, drafting order, and QC after `DESIGN.md` and `TASK.md` are confirmed.

## Input Requirement

The workspace is not ready for project-specific planning until an actual RfP file is present in `01.Input_RfP`. Folder scaffolding alone is not enough to justify task derivation or slide drafting.

## When To Keep Things Generic

Keep the content generic when the RfP does not justify a specific metric, benchmark, example, or implication. Do not fill gaps with assumptions that sound persuasive but are unsupported.
