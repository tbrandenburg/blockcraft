"""Rendering helpers that translate world data into Ursina entities.

We keep rendering separate from the world model. The world knows what blocks
exist, and the renderer knows how to show them in Ursina.
"""

from __future__ import annotations

from typing import Dict, Tuple

from ursina import Entity, color

from blockcraft.game.game_manager import GameManager
from blockcraft.world.blocks import BlockType


class RenderManager:
    """Create and update block entities to match the world data."""

    def __init__(self, game: GameManager) -> None:
        self.game = game
        self.block_entities: Dict[Tuple[int, int, int], Entity] = {}

        # Initial build when the game starts.
        self._rebuild_all()

    def _block_color(self, kind: BlockType):
        if kind == BlockType.GRASS:
            return color.lime
        if kind == BlockType.DIRT:
            return color.brown
        if kind == BlockType.STONE:
            return color.gray
        return color.white

    def _rebuild_all(self) -> None:
        # Remove existing entities
        for e in self.block_entities.values():
            e.disable()
            e.parent = None
        self.block_entities.clear()

        # Create new entities for each block
        for (x, y, z), block in self.game.world.blocks.items():
            self.block_entities[(x, y, z)] = Entity(
                model="cube",
                color=self._block_color(block.kind),
                position=(x, y, z),
                scale=1,
            )

    def sync(self) -> None:
        """Update entities to match current world state.

        For small worlds, we can rebuild everything when counts change.
        For simplicity, we rebuild when the set of coordinates changed.
        """

        coords = set(self.game.world.blocks.keys())
        if coords != set(self.block_entities.keys()):
            self._rebuild_all()
