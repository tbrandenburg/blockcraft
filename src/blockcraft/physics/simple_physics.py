"""Simple physics helpers.

We avoid complexity and only simulate a basic gravity effect that pulls
the player to the ground level.
"""

from __future__ import annotations


class SimplePhysics:
    """Very small physics helper class."""

    def __init__(self, gravity: float = 9.8) -> None:
        # Gravity value is not deeply used; we keep behavior simple.
        self.gravity = gravity

    def apply_gravity(self, y: float, ground_y: float) -> float:
        """Return a y value that does not go below the ground.

        For now, if the player is above ground, we snap to ground.
        This keeps movement simple for beginners.
        """

        if y < ground_y:
            return ground_y
        return y
