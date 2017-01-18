import pytest

from Character import Character
from items import Items


def test_add_encumbrance():
    char = Character("Character", "George", [], description = "A player", keywords = [], race = "Human", sex = "Male", guild = "Paladin", ac = 10, mp = 10, hp = 10, strength = 10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10, level=1, gold=100, xp=0, encumbrance=20, feats=[])
    sword = Items(id = 1, name = "rock", desc = "a rock", long_desc = "a rock", weight = 2, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = ["pebble"], type = "Item")
    sword2 = Items(id = 2, name = "rock", desc = "a rock", long_desc = "a rock", weight = 4, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = ["pebble"], type = "Item")
    assert char.get_encumbrance() == 20
    char.add_encumbrance(sword.get_weight())
    assert char.get_encumbrance() == 22
    char.add_encumbrance(sword2.get_weight())
    assert char.get_encumbrance() == 26

def test_add_encumbrance_if_negative():
    char = Character("Character", "George", [], description="A player", keywords=[], race="Human", sex="Male",
                     guild="Paladin", ac=10, mp=10, hp=10, strength=10, dexterity=10, constitution=10, intelligence=10,
                     wisdom=10, charisma=10, level=1, gold=100, xp=0, encumbrance=20, feats=[])
    sword = Items(id=1, name="rock", desc="a rock", long_desc="a rock", weight=1, value=1, can_pick_up="True",
                  is_magical="True", is_cursed="False", keywords=["pebble"], type="Item")
    assert char.get_encumbrance() == 20
    char.add_encumbrance(sword.get_weight())
    char.add_encumbrance(-(sword.get_weight()))
    assert char.get_encumbrance() == 20

def test_too_heavy_to_pick_up():
    char = Character("Character", "George", [], description="A player", keywords=[], race="Human", sex="Male",
                     guild="Paladin", ac=10, mp=10, hp=10, strength=10, dexterity=10, constitution=10, intelligence=10,
                     wisdom=10, charisma=10, level=1, gold=100, xp=0, encumbrance=20, feats=[])
    sword = Items(id=1, name="rock", desc="a rock", long_desc="a rock", weight=100000, value=1, can_pick_up="True",
                  is_magical="True", is_cursed="False", keywords=["pebble"], type="Item")
    sword2 = Items(id=2, name="rock", desc="a rock", long_desc="a rock", weight=1, value=1, can_pick_up="True",
                   is_magical="True", is_cursed="False", keywords=["pebble"], type="Item")
    assert char.is_too_heavy(sword.get_weight()) == True
    assert char.is_too_heavy(sword2.get_weight()) == False