## MODIFIED Requirements
### Requirement: Basic Player Movement
The system SHALL allow the player to move on the XZ plane using WASD input while the camera orientation controls which direction is forward.

#### Scenario: Move forward relative to camera
- **WHEN** the W key is held
- **THEN** the player's position updates in the direction the camera is facing on the XZ plane

#### Scenario: Move backward relative to camera
- **WHEN** the S key is held
- **THEN** the player's position updates opposite the camera forward direction on the XZ plane

#### Scenario: Move left/right relative to camera
- **WHEN** the A or D keys are held
- **THEN** the player's position updates perpendicular to the camera forward direction on the XZ plane

### Requirement: Mouse Look Camera Control
The system SHALL allow the player to adjust the camera orientation using mouse movement while the game window is focused.

#### Scenario: Horizontal mouse movement
- **WHEN** the player moves the mouse left or right
- **THEN** the camera yaw changes so the view turns in the matching direction

#### Scenario: Vertical mouse movement
- **WHEN** the player moves the mouse up or down
- **THEN** the camera pitch tilts up or down within reasonable limits
