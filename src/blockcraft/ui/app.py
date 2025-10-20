"""Ursina application setup and UI logic.

This module creates the window and connects input (keyboard/mouse)
to the game layer. It avoids putting world or physics rules here.
"""

from __future__ import annotations

import math

from ursina import Ursina, window, camera, Vec3, color, held_keys, mouse, time

from blockcraft.game.game_manager import GameManager, InputState
from blockcraft.ui.render import RenderManager


def run_app() -> None:
    """Create and run the Ursina app.

    We set up a simple camera and a game manager that knows how to
    update the player and world each frame.
    """

    app = Ursina()

    # Make the background color a friendly sky blue.
    window.color = color.rgb(135, 206, 235)

    camera.position = Vec3(0, 5, -10)
    camera.rotation_x = 20

    game = GameManager()
    renderer = RenderManager(game)

    def update():  # Ursina calls this every frame.
        # Collect input from Ursina into a small data class.
        mouse_dx = mouse.velocity[0]
        mouse_dy = mouse.velocity[1]

        input_state = InputState(
            forward=bool(held_keys["w"]),
            back=bool(held_keys["s"]),
            left=bool(held_keys["a"]),
            right=bool(held_keys["d"]),
            mouse_dx=mouse_dx,
            mouse_dy=mouse_dy,
            add_block=bool(mouse.right),
            remove_block=bool(mouse.left),
            dt=time.dt,
        )

        game.update(input_state)
        _update_camera(camera, game)
        renderer.sync()

    app.run()


def _update_camera(camera_obj, game: GameManager) -> None:
    player = game.player
    distance = 6

    yaw_rad = math.radians(player.yaw)
    pitch_rad = math.radians(player.pitch)

    offset_x = distance * math.sin(yaw_rad) * math.cos(pitch_rad)
    offset_y = distance * math.sin(pitch_rad) + 2
    offset_z = distance * math.cos(yaw_rad) * math.cos(pitch_rad)

    camera_obj.position = Vec3(
        player.x - offset_x,
        player.y + offset_y,
        player.z - offset_z,
    )
    camera_obj.look_at(Vec3(player.x, player.y + 2, player.z))
