from blockcraft.world.world import World
from blockcraft.world.blocks import BlockType


def test_generate_flat_ground_creates_blocks():
    world = World(width=4, depth=4)
    world.generate_flat_ground(height=1)
    # 4x4x1 blocks expected
    assert len(world.blocks) == 16


def test_add_and_remove_block_at_player():
    world = World(width=4, depth=4)
    world.generate_flat_ground(height=1)

    # Place a stone block at player's position
    world.add_block_at_player((0.2, 5.0, -0.4), BlockType.STONE)
    assert world.blocks.get((0, 0, 0)) is not None
    assert world.blocks[(0, 0, 0)].kind == BlockType.STONE

    # Remove it
    world.remove_block_at_player((0.2, 5.0, -0.4))
    assert (0, 0, 0) not in world.blocks
