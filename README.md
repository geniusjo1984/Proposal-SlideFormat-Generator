# Proposal-SlideFormat-Generator

Reusable Codex skill for turning user-provided RfP/RFP documents into proposal-slide workspaces, control documents, and one-slide-per-task planning structures.

Korean documentation: [README.ko.md](README.ko.md)

## What This Repo Contains

- `proposal-slideformat-generator/`
  - `SKILL.md`: skill trigger and operating instructions
  - `references/`: reusable templates for `DESIGN.md`, `TASK.md`, `AGENT.md`, and workflow guidance
  - `scripts/init_project.ps1`: workspace scaffolding script

## What The Skill Does

- Create a standard proposal project folder structure
- Stop after scaffolding if the source RfP has not been provided yet
- Generate `DESIGN.md` and `TASK.md` when the user explicitly requests baseline design
- Rebuild `DESIGN.md` from `02.Reference_Templete` when template references exist
- Ask for user confirmation before using the default design baseline when `02.Reference_Templete` is empty
- Generate `AGENT.md` after `DESIGN.md` and `TASK.md` are confirmed
- Treat `TASK.md` as a project-specific output derived from the user's RfP
- Support consulting-style and Korean public-sector proposal slide planning
- Enforce A4 landscape as the fixed default slide ratio

## Install

Clone this repository and copy `proposal-slideformat-generator/` into your Codex skills directory.

```powershell
git clone https://github.com/geniusjo1984/Proposal-SlideFormat-Generator.git
Copy-Item -Recurse -Force .\Proposal-SlideFormat-Generator\proposal-slideformat-generator $HOME\.codex\skills\
```

If you use a Codex skill installer that supports GitHub repositories, install from this repository and select the `proposal-slideformat-generator` skill folder.

## Use

Initialize a new project root folder and standard subfolders:

```powershell
.\proposal-slideformat-generator\scripts\init_project.ps1 -ProjectName client-a-rfp -BasePath .\projects
```

This creates folders only. Then place the source RfP in `01.Input_RfP`.
Then place slide-format references in `02.Reference_Templete` and supporting references in `03` and `04`.

After that, ask Codex to generate baseline `DESIGN.md` and `TASK.md`.

## Repo Notes

- Do not commit client RfPs or internal reference decks unless you have the right to publish them.
- Keep this repository limited to reusable skill logic and templates.
- The repository intentionally excludes screenshots and client-specific sample materials.
