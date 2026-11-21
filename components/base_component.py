from __future__ import annotations

from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity
    from game_map import GameMap

T = TypeVar("T", bound="Entity")

class BaseComponent(Generic[T]):
    parent: T  # Owning entity instance.

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        return self.gamemap.engine