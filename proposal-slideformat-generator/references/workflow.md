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

1. Save the user-provided RfP in `01.Input_RfP`.
2. Collect format references in `02.Reference_Templete`.
3. Collect proposal-content references in `03.Reference_Contents_Main` and `04.Reference_Contents_Assistance`.
4. Create `DESIGN.md` to define slide design and writing rules.
5. Create `TASK.md` from the RfP to define the section hierarchy and slide mapping.
6. Create `AGENT.md` to define execution order, guardrails, and quality checks.
7. Draft slides in `05.Output_Slide`.
8. Revise iteratively without dropping any required source item.

## Document Roles

- `DESIGN.md`: Design authority for layout, color, typography, spacing, and wording style.
- `TASK.md`: Project-specific source of truth for slide planning.
- `AGENT.md`: Execution rules for reading order, drafting order, and QC.

## When To Keep Things Generic

Keep the content generic when the RfP does not justify a specific metric, benchmark, example, or implication. Do not fill gaps with assumptions that sound persuasive but are unsupported.
