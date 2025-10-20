"""Ursina application setup and UI logic.

This module creates the window and connects input (keyboard/mouse)
to the game layer. It avoids putting world or physics rules here.
"""

from __future__ import annotations

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

    # Move the camera a bit up so we can see the ground nicely.
    camera.position = Vec3(0, 10, -20)
    camera.rotation_x = 20

    game = GameManager()
    renderer = RenderManager(game)

    def update():  # Ursina calls this every frame.
        # Collect input from Ursina into a small data class.
        input_state = InputState(
            forward=bool(held_keys["w"]),
            back=bool(held_keys["s"]),
            left=bool(held_keys["a"]),
            right=bool(held_keys["d"]),
            add_block=bool(mouse.right),
            remove_block=bool(mouse.left),
            dt=time.dt,
        )

        game.update(input_state)
        renderer.sync()

    app.run()
