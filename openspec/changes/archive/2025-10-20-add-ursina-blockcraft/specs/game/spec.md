## ADDED Requirements

### Requirement: Basic Player Movement
The system SHALL allow the player to move on the XZ plane using WASD input.

#### Scenario: Move forward
- **WHEN** the W key is held
- **THEN** the player's Z position decreases over time

#### Scenario: Move backward
- **WHEN** the S key is held
- **THEN** the player's Z position increases over time

#### Scenario: Move left/right
- **WHEN** the A or D keys are held
- **THEN** the player's X position changes left/right over time

### Requirement: Block Interaction
The system SHALL support adding or removing a block at the player's ground position.

#### Scenario: Add block
- **WHEN** right mouse button is pressed
- **THEN** a block of the selected type is placed at the player's ground position

#### Scenario: Remove block
- **WHEN** left mouse button is pressed
- **THEN** the block at the player's ground position is removed if it exists
