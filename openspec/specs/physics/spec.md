# physics Specification

## Purpose
TBD - created by archiving change add-ursina-blockcraft. Update Purpose after archive.
## Requirements
### Requirement: Ground Snapping
The system MUST prevent the player from being below the ground level.

#### Scenario: Below ground
- **WHEN** the player's y is below the ground level
- **THEN** the y value is set to the ground level

#### Scenario: Above ground
- **WHEN** the player's y is above the ground level
- **THEN** the y value remains unchanged

