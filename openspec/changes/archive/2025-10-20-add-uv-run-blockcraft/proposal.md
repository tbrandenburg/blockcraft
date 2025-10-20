## Why
Running the game should use the project's standard uv workflow so players can start Blockcraft with a single command.

## What Changes
- Document a change requiring the game to run via `uv run blockcraft`
- Ensure the specs capture the expected command entry point

## Impact
- Affected specs: `specs/game/spec.md`
- Affected code: Game entrypoint script and uv command definition
