# AGENT.md Template

Use this template to create the execution rules for a project-specific proposal workspace after `DESIGN.md` and `TASK.md` are reviewed and confirmed by the user. Use it only when the workspace does not already contain a user-provided `AGENT.md` or the user explicitly asks for regeneration.

This version assumes an HTML-first workflow with one important rule: the first content slide is the calibration slide. Build it carefully, lock the visual pattern, and then generate the remaining slides by reusing that approved structure.

```md
# AGENT.md

## 1. Purpose

This file defines the working rules for agents creating proposal slides in this workspace.

The objective is to:

- use `DESIGN.md` as the visual control document
- use `TASK.md` as the content and slide-mapping control document
- create a proposal-quality HTML slide set that can be exported or moved into PowerPoint/PDF with minimal cleanup

## 2. Preconditions & Read Order

Before generating or revising any slide:

1. Confirm that `01.Input_RfP/` contains the actual source RfP.
2. Confirm that the user has already reviewed and accepted `DESIGN.md` and `TASK.md`.
3. Read materials in this order:
   1. `DESIGN.md`
   2. `TASK.md`
   3. the active RfP in `01.Input_RfP/`
   4. the active user request in the current session

If the RfP is missing, stop and ask the user to place it in `01.Input_RfP/`.

## 3. Source Of Truth

- Primary factual source: `[local RfP path]`
- Design authority: `DESIGN.md`
- Slide planning authority: `TASK.md`
- Optional visual reference authority: `02.Reference_Templete/`

Never add claims, benchmarks, examples, market facts, or implications that are not supported by the source files or explicit user instructions.

## 4. Core Assignment

- Build a proposal-style slide deck covering the confirmed task structure
- Default to one main slide per task unless the user instructs otherwise
- Preserve the governing section hierarchy from `TASK.md`
- Preserve required source bullets and deliverable logic
- Keep the deck suitable for direct PowerPoint export at `A4 landscape`

## 5. Calibration Workflow

### Calibration Slide Rule

The first content slide is the calibration slide.

- Do not use the cover page as the visual standard
- Use either the `전체 과업 프레임워크` slide or the first task slide as the calibration slide
- Build this slide in the final output format with extra care and refine it until the structure is stable

### What Must Be Fixed On The Calibration Slide

Lock the following before moving on:

- upper-context label format
- title placement and top-band treatment
- lead-message style
- core body module style
- box, border, and table treatment
- spacing rhythm
- emphasis color usage
- footer or deliverable strip treatment if used

### Workflow After Calibration

After the first content slide is approved:

1. Reuse the approved title zone and body-module logic
2. Keep the same border, spacing, and label conventions
3. Generate later slides by adapting the approved pattern to each task
4. Only introduce a new layout family when the task type clearly requires it

The goal is deck consistency, not per-slide reinvention.

## 6. Slide Planning Rules

- Use message-driven lead titles
- Add a one-line summary when it improves scan speed
- Keep the body structured and presentation-ready
- Keep slide titles to a single line whenever possible
- Keep all generated readable text at `10pt` or above
- Choose the slide form according to the task type:
  - review/diagnosis: framework, checklist, assessment table
  - execution/process: step flow, input-process-output, swimlane
  - matching/coordination: stakeholder map, matrix, responsibility chart
  - strategy/roadmap: phased roadmap, priority matrix, implementation path
  - analysis/measurement: indicator table, scorecard, evaluation framework
- Avoid paragraph-heavy layouts
- Keep the slide ratio fixed at `A4 landscape` unless the user explicitly overrides it

## 7. Proposal Writing Style

- Write in the language requested by the user
- Maintain a formal consulting or bid-response tone
- Prefer concise, executive-ready phrasing
- Use public-sector or enterprise proposal wording when appropriate
- Avoid slogans, speculative benefits, and unsupported claims
- Favor structured text over narrative explanation

## 8. Content Preservation Rules

For every task slide, preserve:

- the task objective
- the required source bullets
- the execution logic
- the expected deliverable or output
- terminology consistent with the RfP

If `TASK.md` already provides detailed block guidance, use that structure as the baseline rather than inventing a new decomposition.

## 9. HTML Execution Guidance

When generating HTML slides:

- feed both `DESIGN.md` and the relevant task block from `TASK.md` into the generation step
- keep `A4 landscape`, white background, and blue-family emphasis
- preserve the fixed title, lead, body, and footer zones from `DESIGN.md`
- prefer sharp dividers, structured tables, frames, and process diagrams
- keep each slide export-safe and uncluttered
- revise the first content slide until the pattern is solid before batch-producing later slides
- use the user-provided `상단바.svg` directly for the top band; do not redraw, approximate, or restyle the curve in CSS
- keep the upper-context label right-aligned inside the top-band cap with the same right inset as the lead/body area

Default HTML objective:

- take one task from `TASK.md`
- convert it into one proposal-quality slide
- preserve all required sub-items
- align with the approved calibration-slide pattern

## 9A. Output Contract

- use `.html` as the default output format
- save the generated slide artifact in `05.Output_Slide`
- do not switch to Markdown as a slide substitute unless the user explicitly asks for a planning document
- keep the footer/page zone for the page number only
- if a slide exceeds the fixed body zone, split it into another slide rather than shrinking typography below readability

## 10. Quality Control

Before finalizing any slide set, verify:

- every statement is traceable to the RfP or explicit user instruction
- every slide maps to a task in `TASK.md`
- every required `-` level source item is preserved
- upper-context labels are applied consistently
- terminology is consistent across the deck
- tables, matrices, and diagrams remain legible at A4 size
- no element clips at the bottom or edge of the slide
- titles are lead messages rather than noun-only labels
- titles remain single-line wherever possible
- lead messages do not clip at the right edge
- table cells are middle-aligned by default unless the slide requires top-aligned evidence text
- stage or process shapes use discrete dark-to-light palette steps rather than gradients when sequence emphasis is needed
- the visual system stays aligned with `DESIGN.md`
- slides after the first content slide clearly inherit the approved pattern

## 11. Escalation Rule

If the source does not support a claim or detail:

- do not infer aggressively
- do not invent evidence
- stay generic within supported wording
- ask the user for more source material only when necessary
```
