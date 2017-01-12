import pytest
import os

import factory
from Character import Character
from Weapon import Weapon
from factory import Weapon_Factory, Character_Factory


def test_character_loads():
    parsed_json = {
        "name": "Gray Wizard",
        "inventory":[]
    }
    parsed_character = Character_Factory().create(parsed_json)
    character = Character(name = "Gray Wizard", inventory = [])
    assert parsed_character == character


def test_weapon_loads():
    parsed_json = {
        "type": "Weapon",
  "name": "iron longsword",
  "desc": "A short, decently constructed iron longsword.",
  "long_desc": "This longsword does not feel too heavy.  The blade is somewhat rusted on the edges, and the sides are not as keen as they could be.",
  "weight": 8,
  "value": 30,
  "can_pick_up": "True",
  "is_magical": "False",
  "is_cursed": "False",
  "handed" : 1,
  "offhand" : 0,
  "weapon_type": "longsword",
  "const_damage": 0,
  "damage_hit_dice" : 6,
  "damage_hit_dice_coefficient" : 1,
 "damage_stat" : "strength",
   "damage_type" : "slashing",
        "keywords": []

}
    parsed_weapon = Weapon_Factory().create(parsed_json)
    weapon = Weapon(
                    name = "iron longsword",
                    desc= "A short, decently constructed iron longsword.",
                    long_desc= "This longsword does not feel too heavy.  The blade is somewhat rusted on the edges, and the sides are not as keen as they could be.",
                    weight= 8,
                    value= 30,
                    can_pick_up= "True",
                    is_magical= "False",
                    is_cursed= "False",
                    keywords = [],
                    type = "Weapon",
                    handed = 1,
                    offhand = 0,
                    weapon_type= "longsword",
                    const_damage= 0,
                    damage_hit_dice = 6,
                    damage_hit_dice_coefficient = 1,
                    damage_stat = "strength",
                    damage_type = "slashing")
    assert weapon == parsed_weapon