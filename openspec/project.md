# Project Context

## Purpose
Build a simple Minecraft‑like block world game in Python using the Ursina game engine. Focus on approachability for beginners (kids) with clear, readable code and friendly comments while demonstrating basic 3D movement, block placement/removal, and simple physics.

## Tech Stack
- Language: Python (3.10+; target local 3.13 OK)
- Game engine: Ursina
- Package/environment manager: uv (project and venv management)
- Formatter: Black
- Testing: pytest

## Project Conventions

### Code Style
- PEP 8 naming and structure:
  - modules/files: snake_case.py; functions/variables: lower_snake_case; Classes: PascalCase; constants: UPPER_SNAKE_CASE
  - One class per file when practical; keep functions small and descriptive
- Formatting: Black (default settings)
- Comments: Prefer simple, clear, beginner‑friendly explanations; avoid jargon; explain “why” briefly
- Imports: standard lib, third‑party, local (separated by blank lines); absolute imports for clarity
- Avoid cleverness; prefer straightforward, readable code over micro‑optimizations

### Architecture Patterns
- Layered architecture to separate concerns:
  - ui/ — Menus, HUD, user input mapping and simple UI helpers (no game/world logic)
  - game/ — Game loop orchestration, player controller, high‑level rules, event wiring
  - world/ — World data, chunk/grid, blocks, placement/removal, basic generation
  - physics/ — Simple physics helpers (gravity toggle, collision checks)
- Suggested directory structure (under src/):
  - src/
    - ui/
    - game/
    - world/
    - physics/
    - assets/ (optional: textures, sounds)
    - main.py (entry point that composes layers)
- Dependency flow: ui → game → world/physics (no upward imports). world and physics do not import ui.

### Testing Strategy
- Framework: pytest
- Scope: unit tests for world and physics helpers; smoke tests for player/game orchestrations where feasible
- Location: tests/ mirrors src/ structure (e.g., tests/world/test_blocks.py)
- Keep tests small and deterministic; avoid engine window creation in unit tests (abstract where needed)

### Git Workflow
- Branching: Git Flow
  - master: production; develop: integration
  - feature/* branches from develop; merge back via PR
  - release/* from develop; hotfix/* from master
- Commit conventions: Conventional Commits (e.g., feat:, fix:, docs:, refactor:, test:, chore:). Short imperative subject; optional scope (feat(world): add block removal).
- PRs: require at least one review, CI tests passing (when configured)

## Domain Context
General sandbox block building; no special domain rules beyond basic 3D movement and simple block interactions.

## Important Constraints
- Code must be approachable for a 12‑year‑old: simple control flow, descriptive names, and helpful comments
- Keep UI separate from world and physics logic per layered architecture
- Use uv for environment and dependency management
- Use Black for formatting and PEP 8 naming

## External Dependencies
- Ursina (primary engine)
- pytest (testing)
- Black (formatting)
