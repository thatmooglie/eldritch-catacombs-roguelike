from __future__ import annotations

from components.base_component import BaseComponent
from entity import Item
from equipment_types import EquipmentType


class Equippable(BaseComponent[Item]):
    parent: Item

    def __init__(
            self,
            equipment_type: EquipmentType,
            power_bonus: int = 0,
            defence_bonus: int = 0,
        ):

        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self. defence_bonus = defence_bonus


class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)


class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=4)


class LeatherArmour(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOUR, defence_bonus=1)


class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOUR, defence_bonus=3)
