# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- No unreleased changes yet.

## [v0.1.0] - 2026-04-15

### Added

- Added `proposal-slideformat-generator/scripts/generate_calibration_slide.py` for HTML-based calibration and framework slide generation.
- Added an HTML-first fallback workflow for environments where Stitch is unavailable.
- Added explicit A4 fixed-zone slide rules for title, lead, body, divider, and page-number footer handling.
- Added release tagging and GitHub release packaging for the HTML slide baseline.

### Changed

- Updated `AGENT`, `DESIGN`, and `TASK` templates to reflect the approved HTML slide production rules.
- Updated the default skill metadata and workflow guidance to prefer HTML slide artifacts instead of Markdown stand-ins in the fallback path.
- Updated template guidance to require direct use of the user-provided `상단바.svg` asset for the top band.
- Updated body-module rules to keep titles single-line where possible, preserve minimum readable text sizing, middle-align table cells, and apply dark-to-light sequence coloring without gradients.

### Notes

- Local `example/` source assets and generated samples remain excluded from the public repository.
