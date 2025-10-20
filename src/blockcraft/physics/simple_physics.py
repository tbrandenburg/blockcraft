"""Simple physics helpers.

We avoid complexity and only simulate a basic gravity effect that pulls
the player to the ground level.
"""

from __future__ import annotations


class SimplePhysics:
    """Very small physics helper class."""

    def __init__(self, gravity: float = 25.0, damping: float = 0.85) -> None:
        self.gravity = gravity
        self.damping = damping

    def apply_gravity(
        self,
        position: tuple[float, float, float],
        velocity: float,
        ground_y: float,
        dt: float = 1 / 60.0,
    ) -> tuple[float, float, float, float]:
        x, y, z = position

        velocity -= self.gravity * dt
        y += velocity * dt

        if y < ground_y:
            y = ground_y
            velocity = 0.0
        else:
            velocity *= self.damping

        if abs(velocity) < 0.01 and y <= ground_y:
            velocity = 0.0

        return (x, y, z, velocity)
