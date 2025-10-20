## MODIFIED Requirements
### Requirement: Ground Snapping
The system MUST prevent the player from being below the ground level while allowing gravity to pull the player toward the ground.

#### Scenario: Below ground
- **WHEN** the player's y is below the ground level
- **THEN** the y value is set to the ground level and vertical velocity resets

#### Scenario: Above ground
- **WHEN** the player's y is above the ground level
- **THEN** gravity reduces vertical velocity until the player lands on the ground
