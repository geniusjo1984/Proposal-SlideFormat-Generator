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

1. Initialize the workspace folders first.
2. Ask the user to place the source RfP in `01.Input_RfP`.
3. If `01.Input_RfP` has no source file, stop and do not generate `TASK.md` or slides.
4. Collect format references in `02.Reference_Templete`.
5. Collect proposal-content references in `03.Reference_Contents_Main` and `04.Reference_Contents_Assistance`.
6. Create `DESIGN.md` from the fixed design template.
7. Create `TASK.md` from the RfP to define the section hierarchy and slide mapping.
8. Create `AGENT.md` to define execution order, guardrails, and quality checks.
9. Draft slides in `05.Output_Slide`.
10. Revise iteratively without dropping any required source item.

## Document Roles

- `DESIGN.md`: Fixed design authority for A4 landscape layout, color system, typography, spacing, and wording style.
- `TASK.md`: Project-specific source of truth for slide planning.
- `AGENT.md`: Execution rules for reading order, drafting order, and QC.

## Input Requirement

The workspace is not ready for project-specific planning until an actual RfP file is present in `01.Input_RfP`. Folder scaffolding alone is not enough to justify task derivation or slide drafting.

## When To Keep Things Generic

Keep the content generic when the RfP does not justify a specific metric, benchmark, example, or implication. Do not fill gaps with assumptions that sound persuasive but are unsupported.
