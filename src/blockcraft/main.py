"""Game entry point.

This file starts the Ursina app and wires together the UI, game logic,
world data, and simple physics. The goal is clarity over complexity.
"""

from __future__ import annotations

from blockcraft.ui.app import run_app


def main() -> None:
    """Start the game application."""

    # We keep the entry very small and easy to follow.
    run_app()


if __name__ == "__main__":
    main()
