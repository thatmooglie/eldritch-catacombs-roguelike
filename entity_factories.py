from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    colour=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defence=2, base_power=5),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)


cultist = Actor(
    char="c",
    colour=(153, 51, 51),
    name="Cultist",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defence=0, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

ghoul = Actor(
    char='g',
    colour=(170, 170, 96),
    name="Ghoul",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=13, base_defence=1, base_power=6),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=60),
)

shoggoth = Actor(
    char="S",
    colour=(60, 0, 90),
    name="Shoggoth",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defence=3, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100)
)

whispering_stone = Item(
    char="~",
    colour=(207, 63, 255),
    name="Whispering Stone",
    consumable=consumable.ConfusionConsumable(
        number_of_turns=10),
)

invocation_of_the_burning_void= Item(
    char="~",
    colour=(255, 0, 0),
    name="Invocation of the Burning Void",
    consumable=consumable.FireballDamageConsumable(
        damage=12, radius=3),
)

elixir_of_life = Item(
    char="!",
    colour=(127, 0, 255),
    name="Elixir of Life",
    consumable=consumable.HealingConsumable(
        amount=4),
)


flash_of_ra = Item(
    char="~",
    colour=(255, 255, 0),
    name="Flash of Ra",
    consumable=consumable.LightningDamageConsumable(
        damage=20, maximum_range=5),
)


knife = Item(
    char="/",
    colour=(0, 191, 255), 
    name="Knife", 
    equippable=equippable.Dagger()
)


axe = Item(
    char="/", 
    colour=(0, 191, 255), 
    name="Axe", 
    equippable=equippable.Sword()
)


leather_jacket = Item(
    char="[",
    colour=(139, 69, 19),
    name="Leather Jacket",
    equippable=equippable.LeatherArmour()
)


shoggoth_hide = Item(
    char="[",
    colour=(139, 69, 19),
    name="Shoggoth Hide",
    equippable=equippable.ChainMail()
)