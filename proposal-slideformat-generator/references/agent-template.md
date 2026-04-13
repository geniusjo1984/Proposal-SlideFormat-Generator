# AGENT.md Template

Use this template to create the execution rules for a project-specific workspace.

```md
# AGENT.md

## Purpose

Define the working instructions for agents creating proposal slides in this workspace.

## Read Order

Always follow this order before generating or revising slides:

1. Read `DESIGN.md`
2. Read `TASK.md`
3. Read the source RfP in `01.Input_RfP/`
4. Read the active user request in the current session
5. Generate or revise slides only within those constraints

## Source Of Truth

- Primary factual source: `[local RfP path]`
- Design authority: `DESIGN.md`
- Task planning authority: `TASK.md`
- Do not add claims, benchmarks, examples, implications, or interpretation not supported by the source or the current user instruction

## Core Assignment

- Build a proposal-style slide deck covering the RfP task structure
- Use `DESIGN.md` to control visual language and formatting
- Use `TASK.md` to control content structure and slide mapping
- Default to one main slide per task unless the user instructs otherwise

## Slide Planning Rules

- Use message-driven lead titles
- Add a one-line summary when useful
- Keep the body structured and presentation-ready
- Choose the slide form according to the task type
- Avoid paragraph-heavy layouts

## Tone And Writing Style

- Write in the language requested by the user
- Maintain a formal consulting or proposal tone
- Prefer concise, executive-ready wording
- Avoid slogans and speculative benefits

## Quality Control

Before finalizing any slide set, verify:

- every statement is traceable to the source or explicit user instruction
- every slide maps to a task in `TASK.md`
- every required sub-item is preserved
- terminology is consistent
- the layout remains readable at the target size
- slide titles are lead messages

## Escalation Rule

If the source does not support a claim:

- do not infer aggressively
- do not invent evidence
- stay generic within the supported text or ask the user for more source material
```
