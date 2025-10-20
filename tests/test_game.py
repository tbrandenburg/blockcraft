from blockcraft.game.game_manager import GameManager, InputState


def test_player_moves_forward_with_input():
    game = GameManager()
    start_z = game.player.z
    start_x = game.player.x
    game.update(InputState(forward=True, dt=0.5))

    assert game.player.z != start_z or game.player.x != start_x


def test_mouse_input_updates_camera_and_movement_direction():
    game = GameManager()
    game.update(InputState(mouse_dx=1.0, dt=0.2))
    assert game.player.yaw != 0.0

    start_z = game.player.z
    game.update(InputState(forward=True, dt=0.5))
    assert game.player.z < start_z
