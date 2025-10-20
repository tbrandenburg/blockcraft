## MODIFIED Requirements
### Requirement: Ursina App and Rendering
The system SHALL start an Ursina application that displays world blocks and updates them as the world changes while capturing keyboard and mouse input.

#### Scenario: App startup
- **WHEN** the app starts
- **THEN** a window opens with a sky-blue background, a free-look camera, and input capture ready for keyboard and mouse

#### Scenario: Render blocks
- **WHEN** blocks exist in the world
- **THEN** cube entities are shown at their coordinates with simple colors per block type

### Requirement: Input Capture and Camera Updates
The system SHALL capture keyboard states and mouse deltas each frame and pass them to the game manager and camera controller.

#### Scenario: Per-frame input capture
- **WHEN** the update loop runs
- **THEN** keyboard WASD states and mouse delta values are forwarded to the game manager and camera controller
