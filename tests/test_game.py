from blockcraft.game.game_manager import GameManager, InputState


def test_player_moves_forward_with_input():
    game = GameManager()
    start_z = game.player.z
    game.update(InputState(forward=True, dt=0.5))
    assert game.player.z < start_z
