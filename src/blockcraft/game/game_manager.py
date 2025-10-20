"""Game manager coordinates player actions and world updates.

This is where we connect the player to the world and physics. We try to keep
functions short and names descriptive so the code is easy to learn.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, sin, radians

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
    mouse_dx: float = 0.0
    mouse_dy: float = 0.0
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
        self.pitch = 20.0
        self.yaw = 0.0
        self.gravity = True
        self.vertical_velocity = 0.0
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

        self._apply_camera_look(input_state)
        self._apply_movement(input_state)
        self._apply_gravity(input_state.dt)

        # Block interactions: left click removes, right click adds.
        if input_state.remove_block:
            self.world.remove_block_at_player(self.player.position_tuple())
        if input_state.add_block:
            self.world.add_block_at_player(
                self.player.position_tuple(), self.player.selected_block
            )

    def _apply_camera_look(self, input_state: InputState) -> None:
        sensitivity = 60.0
        self.player.yaw += input_state.mouse_dx * sensitivity * input_state.dt
        self.player.pitch -= input_state.mouse_dy * sensitivity * input_state.dt
        self.player.pitch = max(-80.0, min(80.0, self.player.pitch))

    def _apply_movement(self, input_state: InputState) -> None:
        move_speed = self.player.speed
        move_amount = move_speed * input_state.dt

        yaw_rad = radians(self.player.yaw)
        forward_vec = (sin(yaw_rad), -cos(yaw_rad))
        right_vec = (forward_vec[1], -forward_vec[0])

        move_x = 0.0
        move_z = 0.0

        if input_state.forward:
            move_x += forward_vec[0]
            move_z += forward_vec[1]
        if input_state.back:
            move_x -= forward_vec[0]
            move_z -= forward_vec[1]
        if input_state.right:
            move_x += right_vec[0]
            move_z += right_vec[1]
        if input_state.left:
            move_x -= right_vec[0]
            move_z -= right_vec[1]

        length_sq = move_x * move_x + move_z * move_z
        if length_sq > 0:
            length = length_sq ** 0.5
            move_x = (move_x / length) * move_amount
            move_z = (move_z / length) * move_amount

            self.player.x += move_x
            self.player.z += move_z

    def _apply_gravity(self, dt: float) -> None:
        if not self.player.gravity:
            return

        self.player.x, self.player.y, self.player.z, self.player.vertical_velocity = (
            self.physics.apply_gravity(
                position=(self.player.x, self.player.y, self.player.z),
                velocity=self.player.vertical_velocity,
                ground_y=self.world.ground_level(),
                dt=dt,
            )
        )
