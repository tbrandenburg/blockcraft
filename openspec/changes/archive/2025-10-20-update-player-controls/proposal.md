## Why
Players currently cannot move or adjust the camera, leaving the game unplayable. We need to support the expected WASD movement and mouse-driven camera look.

## What Changes
- Update the game loop to read keyboard/mouse input and move the player on the XZ plane
- Add mouse look support so moving the mouse changes the viewing direction
- Ensure inputs are wired through the UI layer into the game manager

## Impact
- Affected specs: `specs/game/spec.md`, `specs/ui/spec.md`, `specs/physics/spec.md`
- Affected code: `blockcraft/ui/app.py`, `blockcraft/game/game_manager.py`, `blockcraft/physics/simple_physics.py`, new camera control helpers
