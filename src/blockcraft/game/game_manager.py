"""Game manager coordinates player actions and world updates.

This is where we connect the player to the world and physics. We try to keep
functions short and names descriptive so the code is easy to learn.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from blockcraft.world.world import World
from blockcraft.world.blocks import BlockType
from blockcraft.physics.simple_physics import SimplePhysics


@dataclass
class InputState:
    """Very simple input data coming from the UI layer.

    We keep only what we need: movement directions, mouse actions, and dt.
    """

    forward: bool = False
    back: bool = False
    left: bool = False
    right: bool = False
    add_block: bool = False
    remove_block: bool = False
    dt: float = 0.0

class Player:
    """Very simple player state.

    We only track position and a selected block type for building.
    """

    def __init__(self) -> None:
        self.x = 0.0
        self.y = 5.0
        self.z = 0.0
        self.speed = 10.0
        self.selected_block: BlockType = BlockType.GRASS

    def position_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)


class GameManager:
    """Holds main game objects and runs per-frame updates."""

    def __init__(self) -> None:
        self.world = World(width=20, depth=20)
        self.physics = SimplePhysics()
        self.player = Player()

        # Create a flat world at y = 0.
        self.world.generate_flat_ground(height=1)

    def update(self, input_state: InputState) -> None:
        """Called every frame to update game state."""

        self._handle_player_input(input_state)

    def _handle_player_input(self, input_state: InputState) -> None:
        """Move the player based on held keys.

        We keep controls simple: WASD to move on the ground plane.
        """

        move_amount = self.player.speed * input_state.dt

        if input_state.forward:  # forward (decrease z)
            self.player.z -= move_amount
        if input_state.back:  # backward (increase z)
            self.player.z += move_amount
        if input_state.left:  # left (decrease x)
            self.player.x -= move_amount
        if input_state.right:  # right (increase x)
            self.player.x += move_amount

        # Apply basic gravity so the player stays on ground.
        self.player.y = self.physics.apply_gravity(
            y=self.player.y, ground_y=self.world.ground_level()
        )

        # Block interactions: left click removes, right click adds.
        if input_state.remove_block:
            self.world.remove_block_at_player(self.player.position_tuple())
        if input_state.add_block:
            self.world.add_block_at_player(
                self.player.position_tuple(), self.player.selected_block
            )
