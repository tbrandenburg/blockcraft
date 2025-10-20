## Why
Introduce a simple, kid-friendly Minecraft-like game to demonstrate layered architecture in Python using Ursina, with uv-managed dependencies, readable code, and basic tests.

## What Changes
- Create a new Python package `blockcraft` with layers: `ui`, `game`, `world`, `physics`.
- Add `pyproject.toml` for uv, dependencies (Ursina) and dev tools (pytest, Black).
- Implement minimal world model (flat ground, add/remove blocks), simple physics (ground snapping), game manager (input-driven movement), and UI/renderer in Ursina.
- Add basic pytest tests for world, physics, and a small game movement check.

## Impact
- Affected specs: `game`, `world`, `physics`, `ui`.
- Affected code: `src/blockcraft/**`, `pyproject.toml`, `tests/**`.
- No breaking changes (net-new capability).
