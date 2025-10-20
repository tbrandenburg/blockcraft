from blockcraft.physics.simple_physics import SimplePhysics


def test_apply_gravity_keeps_above_ground():
    physics = SimplePhysics()
    # Player below ground snaps up to ground level
    assert physics.apply_gravity(y=-5.0, ground_y=0.0) == 0.0

    # Player above ground stays as is (no extra falling in this simple model)
    assert physics.apply_gravity(y=3.0, ground_y=0.0) == 3.0
