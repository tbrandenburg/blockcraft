"""Block definitions.

We only need a few simple block types for a tiny game.
"""

from __future__ import annotations

from enum import Enum


class BlockType(str, Enum):
    GRASS = "grass"
    DIRT = "dirt"
    STONE = "stone"


DEFAULT_BLOCK = BlockType.GRASS
