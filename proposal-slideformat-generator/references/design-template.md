# DESIGN.md Template

Use this template as the default design baseline when `02.Reference_Templete` has no usable design reference. Treat the visual rules below as the default standard, not as optional suggestions. The document structure follows the common `awesome-design-md` table of contents, while the actual content is adapted for Korean consulting-style proposal slides rather than product UI.

```md
# DESIGN.md

This design system applies to slides created from the source document below and the user instruction provided in this session.

- Source document: `[set the local RfP path here]`
- Reference template folder: `02.Reference_Templete`
- Source rule: do not add claims, data, examples, or interpretations beyond the provided material unless the user explicitly asks

## 1. Visual Theme & Atmosphere

This deck should feel like a board-ready consulting proposal for a Korean public-sector or enterprise bid. The visual language is formal, analytical, and tightly structured. It should resemble a disciplined report document rather than a startup landing page, SaaS dashboard, or marketing brochure.

The page canvas is pure white (`#FFFFFF`) and should remain dominant across the deck. Visual authority comes from layout discipline, linework, hierarchy, and restrained blue-family emphasis rather than heavy fills or decorative effects. The overall impression should be crisp, flat, document-like, and information-dense without becoming cluttered.

What defines the atmosphere:

- message-driven titles instead of noun-only labels
- compact title band with upper-context label and divider
- structured analytical modules such as tables, process blocks, matrices, timelines, roadmaps, and evidence boxes
- thin borders and separators instead of heavy chrome
- compact but legible body copy
- stable, repeatable visual logic from slide to slide
- public-sector proposal density rather than airy presentation spacing
- fixed-zone composition based on the first-page template frame so title, lead, body, and footer never collide

## 2. Color Palette & Roles

### Primary

- Background White: `#FFFFFF`
- Text Black: `#000000`
- Deep Navy: `#1D2E4F`
- Primary Blue: `#006DBB`
- Bright Cyan Blue: `#03B1E7`

### Supporting

- Alert Red: `#C00000`
- Border Gray: `#D7DBDF`
- Surface Gray: `#F4F5F6`
- Secondary Navy: `#30558C`
- Secondary Blue: `#3278B8`
- Neutral Gray: `#5A5A5B`

### Role Rules

- Use `#1D2E4F` for main titles, key headers, and primary structural emphasis
- Use `#006DBB` for highlights, sequence markers, and active emphasis
- Use `#03B1E7` sparingly for secondary differentiation
- Use gray tones for borders, subtle fills, captions, and low-priority grouping
- Use red only for risk, caution, issue, or contrast explicitly supported by the source
- Keep large background fills minimal so white remains the dominant canvas

## 3. Typography Rules

### Font Family

- Primary title font: `KoPub돋움체 Bold`
- Primary body font: `KoPub돋움체 Medium`
- Supporting font: `KoPub돋움체 Light`
- Fallback title font: `Pretendard Bold`
- Fallback body font: `Pretendard Medium`
- Fallback supporting font: `Pretendard Regular`

### Hierarchy

- Title: bold, compact, highly legible, single-line mandatory, approximately `24pt` as the baseline reference
- Lead message: medium weight, one concise line when used, approximately `16pt` as the baseline reference
- Section label / module header: short noun phrase, medium or bold
- Stage micro-label / step label: compact label, approximately `9pt`
- Card title / module title: approximately `14pt` when used in stage cards or explanatory cards
- Body text: optimized for dense reading in tables, matrices, and structured modules
- Caption / note: light or regular, only when necessary
- Minimum readable size for generated slide text: `10pt`

### Typesetting Principles

- Keep type hierarchy crisp and restrained
- Prefer short, high-signal sentences and concise bullets
- Do not use expressive display typography
- All line breaks must occur at word boundaries
- Do not split Korean eojeol across lines
- Align numbers, labels, and column headings cleanly in tables and scorecards
- Keep stage labels, numbered badges, and card captions visibly smaller than the main title system
- Use bold mainly for the title, module headers, and key labels; keep body copy medium-weight for readability
- Do not drop below `10pt` for body, table, card, footer-page, or stage text in generated slides

## 4. Component Stylings

### Upper Context

- Place a clear upper-context label within the title band when the slide belongs to a broader section
- Preferred placement is the upper-right cap area attached to the top navy bar
- Preferred format: `Ⅰ. 대분류`, `1. 물품∙유통 구조 파악 I (1)`, or equivalent section-task notation
- Use a smaller size than the title but keep it clearly visible
- The upper-context label should act as navigational metadata, not as a decorative subtitle
- Keep placement consistent across the deck so evaluators can immediately understand the current section and task location

### Top Band

- Reserve a stable top band across all slides for upper-context label, title, lead message, and divider
- Do not allow the top band to collapse or vary dramatically from slide to slide
- Keep the top band compact; do not turn it into a cover-style hero zone
- The top band should read in this order:
  - main title
  - upper-context label
  - optional one-line lead message
  - thin divider
- In practice, the title is usually upper-left and the upper-context label is upper-right within the same band
- The divider should span most of the content width and visually separate framing from analysis
- When the reference template is used, the separator should follow the template form exactly: use the top border of the body frame as the visual divider rather than inventing a separate decorative line
- The top band should visually inherit the first-page template form:
  - title anchored from the upper-left margin, not centered
  - use the user-provided `상단바.svg` as the top-band shape exactly as provided
  - place the upper-context label on top of that asset rather than rebuilding the bar and cap separately
  - no extra decorative bar, shadow, or color variation beyond this template form
- The upper-context label must sit cleanly inside the right-side cap and must not drop into the lead-message line or body zone
- The vertical gap between the title box and the top horizontal bar must be `0.25cm` (`7.1pt`)
- The horizontal bar height, excluding the taller right-side cap area, must be `0.1cm` (`2.84pt`)
- The upper-context label text should be right-aligned, and its right inset must match the right inset used by the lead-message zone and body frame

### Title

- Use message-driven lead titles rather than noun-only headings
- Keep the title to one line whenever possible
- The title should state the core takeaway, task logic, or proposal stance directly
- Avoid long descriptive sentences; compress the message to proposal-ready phrasing
- Use strong visual emphasis through weight and placement, not through excessive size inflation

### Lead Message

- Use the lead message as a one-line interpretive sentence directly below the title when the slide benefits from a stated conclusion
- The lead message should explain what the slide proves, proposes, or prioritizes
- Keep it shorter and visually lighter than the title
- Do not repeat the title verbatim; the lead message should add interpretation or framing
- If the slide is already self-evident through title and body structure, omit the lead message rather than forcing it
- Use black text on a white background for the lead message unless the user explicitly requests a filled highlight bar
- Anchor the lead-message zone with left and right insets instead of a hard-coded width so the right edge does not clip on A4 export
- Do not combine a fixed one-line lead width with `overflow: hidden`; if the sentence is long, allow a controlled wrap inside the lead-message zone

### Body

- The body should occupy the main analytical zone and contain one dominant structure only
- Choose the body form based on the message:
  - structured table for criteria, comparison, deliverables, or review items
  - process flow for execution sequence, stage logic, or operational steps
  - matrix for segmentation, prioritization, or matching logic
  - input-process-output for methodology or workstream explanation
  - stakeholder map for roles, coordination, and governance
  - roadmap or timeline for phased execution and future-state transition
  - checklist or scorecard for diagnosis, assessment, and validation
- Avoid mixing multiple equally dominant body structures on one slide
- Keep the body visually modular so each block has a clear role: `목적`, `대상`, `기준`, `실행`, `결과`, `산출물`
- For framework slides, prefer a top stage ribbon or stage row plus one dominant analysis area below
- For denser proposal pages, a left explanatory block plus right table/evidence block pattern is preferred over freeform box scattering

### Body Modules

- Prefer rectangular, grid-aligned modules with thin borders
- Keep module headers short and scannable
- Use pale gray or very light blue fills only when grouping improves readability
- Emphasize hierarchy with alignment, spacing, header rules, key numbers, and label weight before adding color
- Keep cell padding and internal spacing tight but not cramped
- Tables, matrices, and scorecards should prioritize scan speed over prose completeness
- In tables, the default vertical alignment of header and body cells should be middle-aligned unless a specific slide requires top-aligned multi-line evidence text
- If icons are used, they must clarify meaning immediately; avoid decorative icon sets
- Explanatory mini-cards may use a narrow vertical blue accent strip on the left with a white card body
- Stage cards should keep even widths and consistent heights when repeated across a row
- Use numbered circles or sequence badges only when the slide communicates an actual staged sequence
- Important point labels inside body modules should be expressed as filled color chips or header tabs with white text when emphasis is required
- If a row of repeated shapes represents stages, process flow, or phased progression, assign the shapes different fills or accents from the approved palette so they read from darker to lighter across the sequence
- Do not use a gradient fill; use discrete per-shape colors from the specified navy-blue family to show direction and flow

### Bottom Band

- Use the bottom zone only when it adds decision value
- Typical bottom-band roles:
  - expected deliverables
  - execution implications
  - key decision points
  - closing takeaway
  - source-backed caution or assumption note
- Keep the bottom band visually lighter than the main body
- Do not turn the bottom band into a second full content area
- If no useful closing strip exists, leave the space to preserve readability
- Small support cards or implication boxes are acceptable in the bottom zone when they do not compete with the main body

### Side Notes And Callouts

- Use side callouts only when they sharpen interpretation, not to compensate for weak main structure
- Callouts should be short and tightly anchored to the relevant body module
- Risk, issue, or caution callouts may use red sparingly if supported by the source
- Supporting callouts should never overpower the title or body logic

### Styling Rules

- Use thin, sharp borders and separators
- Keep boxes rectangular and disciplined
- Use fills sparingly and mainly in pale gray or very light blue
- Emphasize with header bars, side rules, key numbers, or highlighted labels rather than large saturated areas
- Maintain stable spacing rhythm between top band, body, and bottom band
- Keep the same visual treatment for repeated component types across the deck
- Avoid decorative chrome, heavy shadows, or ornamental flourishes that do not improve comprehension

## 5. Layout Principles

- Slide ratio is mandatory: `A4 landscape`
- Target page size: `297mm x 210mm`
- Point reference size for export/layout math: approximately `841.9pt x 595.3pt`
- Do not use `16:9` composition for this engagement
- Reserve a stable top band for upper-context label, title, optional lead line, and divider
- Keep title/lead spacing compact and controlled
- Organize content so the reasoning flows left-to-right or top-to-bottom
- Prefer a predictable internal grid instead of freeform collage layouts
- Keep outer margins generous enough to avoid export clipping
- Recommended zoning:
  - top 12-18% for context label, title, lead line, divider
  - middle 62-72% for the main analytical body
  - bottom 10-18% for execution notes, deliverables, or closing implication when needed
- One clear headline message per slide
- One dominant analytical structure per slide
- Favor structured layouts such as tables, flowcharts, matrices, scorecards, and roadmaps over paragraph-heavy compositions
- Choose the slide form according to the message and evidence rather than forcing a single layout pattern everywhere
- When using repeated modules, keep widths regular and spacing rhythmic rather than visually improvising each box

## 5A. HTML Fixed-Zone Contract

For HTML output, use the first page of the provided proposal template as the layout contract. Treat this as a fixed composition frame, not as an approximate mood board.

### Reference Canvas

- Final output canvas: actual `A4 landscape`, approximately `841.9pt x 595.3pt`
- Template reference frame: `780pt x 540pt`
- Use the template only as a positional reference and remap its zones onto the A4 canvas
- Recommended implementation: one fixed A4 slide container with explicit coordinates, scaled only for preview
- Default final output format is `.html`

### Zone Definitions

- `Title Band`
  - overall vertical band: `y = 0pt ~ 63.9pt`
  - main title safe box: `x = 0pt ~ 591.1pt`, `y = 0pt ~ 51.8pt`
  - upper-context label safe box: `x = 598.0pt ~ 818.7pt`, `y = 48.5pt ~ 63.9pt`
  - purpose: headline and section metadata only
  - the title safe box bottom edge must stay `0.25cm` (`7.1pt`) above the top horizontal bar
  - the top horizontal bar itself must remain `0.1cm` (`2.84pt`) high except for the taller right-side cap
  - the upper-context text must align to the same right inset as the lead-message and body zones, not to the canvas edge
- `Lead Message Zone`
  - box: `x = 53.7pt ~ 788.1pt`, `y = 78.5pt ~ 122.6pt`
  - height budget: `44.1pt`
  - purpose: one-line or tightly wrapped interpretive message only
- `Divider / Frame Boundary`
  - template-form divider: the top edge of the body frame
  - line start: `x = 23.2pt`
  - line end: `x = 818.7pt`
  - line position: `y = 141.3pt`
  - do not replace this with a decorative custom divider
- `Body Zone`
  - box: `x = 23.2pt ~ 818.7pt`, `y = 141.3pt ~ 566.3pt`
  - size: `795.5pt x 425.0pt`
  - purpose: the single dominant analytical structure
- `Footer / Page Zone`
  - box: `x = 23.2pt ~ 818.7pt`, `y = 566.3pt ~ 595.3pt`
  - height budget: `29.0pt`
  - purpose: page number only

### Non-Overlap Rules

- No title text may extend below `y = 63.9pt`
- No lead-message text may extend below `y = 122.6pt`
- No body element may start above `y = 141.3pt`
- No body element may extend below `y = 566.3pt`
- Footer content must stay inside the footer/page zone and should not rise into the body zone
- The footer/page zone must contain only the page number; do not place takeaway text, source notes, captions, or metadata there
- If content exceeds the body zone, split the slide rather than compressing typography past readability

### HTML Implementation Rules

- Use absolute or grid-based placement tied to the fixed reference frame
- Define explicit CSS variables for title band, lead zone, body zone, and footer zone
- Use the user-provided `상단바.svg` as a fixed layout asset and position title/upper-context text on top of it
- Reserve the body frame before inserting content; do not let content auto-push the footer downward
- Use `overflow: hidden` only as a last-resort safeguard, not as the primary layout strategy
- Treat the body frame top border as the required separator form from the template
- Keep the page-number area reserved at the bottom-right even when a page number is omitted on draft slides
- Align the page number to the bottom-right within the reserved footer/page zone
- For lead-message placement, prefer `left` + `right` anchoring over `left` + fixed `width`
- For emphasized module labels inside the body, use filled navy or blue chips with white text instead of plain black labels
- Keep `상단바.svg` scaling proportional and do not alter its curve, shoulder, or cap form

## 6. Depth & Elevation

The deck should feel mostly flat and document-like. Depth is not created through soft shadows or layered 3D treatment. Instead, visual separation should come from spacing, borders, alignment, and occasional subtle fills.

Preferred depth treatment:

- Flat white background as the default page layer
- Thin border lines in `#D7DBDF` for structural separation
- Very light fills such as `#F4F5F6` only for grouping or row emphasis
- No gradient backgrounds
- No glassmorphism
- No heavy drop shadows
- No decorative depth effects that reduce print/export clarity

## 7. Do's and Don'ts

### Do

- use message-driven titles
- keep every slide presentation-ready at A4 size
- keep HTML slides locked to the fixed zone contract from the template first page
- privilege logic, readability, and export safety
- maintain consistent title-zone, divider, and module spacing treatment
- build slides from structured modules rather than paragraphs
- use blue-family accents consistently across the deck
- preserve continuity across slides through stable label placement and repeated module styling
- reuse the first approved title-band and stage-ribbon treatment across subsequent slides when applicable

### Don't

- do not change the background away from white
- do not default to colorful startup-style layouts, gradients, soft shadows, or playful illustrations
- do not use noun-only slide titles when a supported lead message can be written
- do not overload slides with prose
- do not stack too many equally weighted boxes without clear hierarchy
- do not use bright colors decoratively
- do not let any element clip near the bottom or edges of the A4 frame
- do not let each slide invent a new visual language
- do not replace stage rows with oversized chevrons, glossy smart-art, or decorative pill tabs
- do not use thick borders or heavy fill blocks where thin separators and white cards communicate the structure more clearly
- do not let auto-height HTML sections push title, body, and footer into each other

## 8. Responsive Behavior

These slides are designed primarily for fixed-size proposal output rather than responsive web rendering. The equivalent rule is layout stability across export and review contexts.

- Keep all core content readable at A4 landscape size
- Ensure tables, matrices, and diagrams remain legible when exported to PowerPoint or PDF
- Avoid overly dense bottom regions that may clip during export
- Keep title lengths controlled so line wrapping does not break hierarchy
- If content exceeds one slide comfortably, split the logic rather than compressing the typography excessively

## 9. Agent Prompt Guide

When using this file for Stitch or other slide-generation workflows, treat it as the controlling visual brief.

- Use this design system for all slides derived from `[set the local RfP path here]`
- Keep the slide ratio fixed at `A4 landscape`
- For HTML output, preserve the template first-page frame based on the fixed `780pt x 540pt` reference canvas
- Use `.html` as the default final output unless the user explicitly asks for another slide-native format
- Use white background only
- Use the specified blue-family palette as the main emphasis system
- Prefer structured consulting layouts such as tables, matrices, process flows, checklists, timelines, and roadmaps
- Write titles as lead messages, not noun-only labels
- Keep slides formal, analytical, and public-sector proposal-ready
- If `KoPub돋움체` is unavailable, use `Pretendard` as the fallback
- When generating a deck, create the first content slide carefully and reuse its approved structure across later slides
- In HTML, explicitly reserve title band, lead-message zone, body zone, and footer/page zone before inserting content
- Use the user-provided `상단바.svg` directly and do not approximate the top band with CSS boxes or substitute shapes
- If `02.Reference_Templete` contains a usable client or bid reference deck, tighten this baseline toward that reference while preserving the fixed rules in this document
```
