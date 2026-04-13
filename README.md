# Proposal-SlideFormat-Generator

Reusable Codex skill for turning user-provided RfP/RFP documents into proposal-slide workspaces, control documents, and one-slide-per-task planning structures.

## What This Repo Contains

- `proposal-slideformat-generator/`
  - `SKILL.md`: skill trigger and operating instructions
  - `references/`: reusable templates for `DESIGN.md`, `TASK.md`, `AGENT.md`, and workflow guidance
  - `scripts/init_project.ps1`: workspace scaffolding script

## What The Skill Does

- Create a standard proposal project folder structure
- Generate baseline `DESIGN.md`, `TASK.md`, and `AGENT.md`
- Treat `TASK.md` as a project-specific output derived from the user's RfP
- Support consulting-style and Korean public-sector proposal slide planning

## Install

Clone this repository and copy `proposal-slideformat-generator/` into your Codex skills directory.

```powershell
git clone https://github.com/<your-account>/Proposal-SlideFormat-Generator.git
Copy-Item -Recurse -Force .\Proposal-SlideFormat-Generator\proposal-slideformat-generator $HOME\.codex\skills\
```

If you use a Codex skill installer that supports GitHub repositories, install from this repository and select the `proposal-slideformat-generator` skill folder.

## Use

Initialize a new project root folder and standard subfolders:

```powershell
.\proposal-slideformat-generator\scripts\init_project.ps1 -ProjectName client-a-rfp -BasePath .\projects
```

Or scaffold directly into a known target path:

```powershell
.\proposal-slideformat-generator\scripts\init_project.ps1 -ProjectRoot .\projects\client-a-rfp
```

Create `개요.md` only when needed:

```powershell
.\proposal-slideformat-generator\scripts\init_project.ps1 -ProjectRoot .\projects\client-a-rfp -IncludeOverview
```

## Repo Notes

- Do not commit client RfPs or internal reference decks unless you have the right to publish them.
- Keep this repository limited to reusable skill logic and templates.
