# game Specification

## Purpose
TBD - created by archiving change add-ursina-blockcraft. Update Purpose after archive.
## Requirements
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

### Requirement: UV Run Command Launches Game
The system SHALL expose a `uv run blockcraft` command that launches the Blockcraft game entry point.

#### Scenario: Launch game from command
- **WHEN** a player runs `uv run blockcraft`
- **THEN** the Blockcraft game window opens and the game loop starts

