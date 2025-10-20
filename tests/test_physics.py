from blockcraft.physics.simple_physics import SimplePhysics


def test_apply_gravity_simulates_fall_and_ground_snap():
    physics = SimplePhysics()
    _, y, _, velocity = physics.apply_gravity(
        position=(0.0, 5.0, 0.0), velocity=0.0, ground_y=0.0, dt=0.1
    )

    assert y < 5.0
    assert velocity < 0.0

    _, ground_y_result, _, velocity = physics.apply_gravity(
        position=(0.0, -1.0, 0.0), velocity=-2.0, ground_y=0.0, dt=0.1
    )
    assert ground_y_result == 0.0
    assert velocity == 0.0
