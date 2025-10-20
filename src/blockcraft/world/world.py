"""World data and helpers.

To keep things simple, we store blocks in a dictionary using integer
grid coordinates. We also offer very basic helpers for adding and
removing blocks near the player.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from blockcraft.world.blocks import BlockType, DEFAULT_BLOCK


Int3 = Tuple[int, int, int]


@dataclass
class Block:
    """Represents a block in the world at integer coordinates."""

    x: int
    y: int
    z: int
    kind: BlockType


class World:
    """Very small block world stored in memory.

    This does not draw anything by itself. Rendering is handled by Ursina
    entities in the UI layer.
    """

    def __init__(self, width: int = 16, depth: int = 16) -> None:
        self.width = max(1, width)
        self.depth = max(1, depth)
        self.blocks: Dict[Int3, Block] = {}

    def generate_flat_ground(self, height: int = 1) -> None:
        """Create a flat platform centered around (0, 0)."""

        half_w = self.width // 2
        half_d = self.depth // 2
        for x in range(-half_w, half_w):
            for z in range(-half_d, half_d):
                for y in range(height):
                    self.blocks[(x, y, z)] = Block(x=x, y=y, z=z, kind=DEFAULT_BLOCK)

    def ground_level(self) -> float:
        """Return the y height of the top ground layer.

        We use this for very basic gravity.
        """

        # If height is 1, the top is y=0.
        return 0.0

    def _player_to_grid(self, pos: tuple[float, float, float]) -> Int3:
        px, py, pz = pos
        return (int(round(px)), int(round(py)), int(round(pz)))

    def add_block_at_player(self, player_pos: tuple[float, float, float], kind: BlockType) -> None:
        """Add a block near the player on the ground level.

        To keep it simple, we place the block directly under the player's feet
        (on ground level), ignoring complex aiming or ray casts.
        """

        gx, _, gz = self._player_to_grid(player_pos)
        gy = int(self.ground_level())
        self.blocks[(gx, gy, gz)] = Block(x=gx, y=gy, z=gz, kind=kind)

    def remove_block_at_player(self, player_pos: tuple[float, float, float]) -> None:
        """Remove the block under the player if it exists."""

        gx, _, gz = self._player_to_grid(player_pos)
        gy = int(self.ground_level())
        self.blocks.pop((gx, gy, gz), None)
