from race import Race
from race_loader import race_from_dict, race_to_dict


def test_race_exists():
    parsed_json = {"name": "Dwarf",
                   "desc": "A short, stout dwarf with a majestic beard.",
  "light_level": 25,
  "size": 1,
                   "attributes": {
                       "STR": 0,
                       "CON": 2,
                       "DEX": 0,
                       "WIS": 0,
                       "CHA": -2,
                       "INT": 0
                   },
                  "body_type":  {
            "Main Hand": "Nothing",
            "Off Hand": "Nothing",
            "Head": "Nothing",
            "Neck": "Nothing",
            "Body" : "Nothing",
            "Back" : "Nothing",
            "Waist": "Nothing",
            "Hands" : "Nothing",
            "Feet": "Nothing",
            "Ring Slot 1": "Nothing",
            "Ring Slot 2": "Nothing",
        "Bag Slot": "Nothing"
        }

                   }
    parsed_race = race_from_dict(parsed_json)
    race = Race(name = "Dwarf", desc = "A short, stout dwarf with a majestic beard.", light_level=25, size=1, strength = 0, constitution=2, dexterity=0,intelligence=0,charisma=-2,wisdom=0, body_type={
            "Main Hand": "Nothing",
            "Off Hand": "Nothing",
            "Head": "Nothing",
            "Neck": "Nothing",
            "Body" : "Nothing",
            "Back" : "Nothing",
            "Waist": "Nothing",
            "Hands" : "Nothing",
            "Feet": "Nothing",
            "Ring Slot 1": "Nothing",
            "Ring Slot 2": "Nothing",
        "Bag Slot": "Nothing"
        })
    assert parsed_race == race

def test_race_dict_translates_to_object():
    parsed_json = {"name": "Dwarf",
                   "desc": "A short, stout dwarf with a majestic beard.",
  "light_level": 25,
  "size": 1,
                   "attributes": {
                       "STR": 0,
                       "CON": 2,
                       "DEX": 0,
                       "WIS": 0,
                       "CHA": -2,
                       "INT": 0
                   },
                  "body_type":  {
            "Main Hand": "Nothing",
            "Off Hand": "Nothing",
            "Head": "Nothing",
            "Neck": "Nothing",
            "Body" : "Nothing",
            "Back" : "Nothing",
            "Waist": "Nothing",
            "Hands" : "Nothing",
            "Feet": "Nothing",
            "Ring Slot 1": "Nothing",
            "Ring Slot 2": "Nothing",
        "Bag Slot": "Nothing"
        }

                   }
    parsed_race = race_from_dict(parsed_json)
    race = Race(name="Dwarf", desc="A short, stout dwarf with a majestic beard.", light_level=25, size=1, strength=0,
                constitution=2, dexterity=0, intelligence=0, charisma=-2, wisdom=0, body_type={
            "Main Hand": "Nothing",
            "Off Hand": "Nothing",
            "Head": "Nothing",
            "Neck": "Nothing",
            "Body": "Nothing",
            "Back": "Nothing",
            "Waist": "Nothing",
            "Hands": "Nothing",
            "Feet": "Nothing",
            "Ring Slot 1": "Nothing",
            "Ring Slot 2": "Nothing",
            "Bag Slot": "Nothing"
        })
    assert parsed_race == race


def test_inverse():
    race = Race("Human", "George", light_level=1, size = 1, strength=0, constitution=0, dexterity=0, intelligence=0, wisdom=0, charisma=0, body_type = {})
    serialized_race = race_to_dict(race)
    expected = {"name": "Human",
                   "desc": "George",
                "light_level": 1,
                "size": 1,
                "body_type" : {},
                   "attributes": {
                       "STR": 0,
                       "CON": 0,
                       "DEX": 0,
                       "WIS": 0,
                       "CHA": 0,
                       "INT": 0
                   }

                   }
    assert serialized_race == expected

def test_inverse_attributes():
    expected = {"name": "Human",
                   "desc": "George",
                "light_level": 1,
                "size": 1,
                "body_type": {},
                   "attributes": {
                       "STR": 1,
                       "CON": 2,
                       "DEX": 3,
                       "WIS": 4,
                       "CHA": 5,
                       "INT": 6
                   }

                   }
    race = Race("Human", "George", light_level= 1, size =1, body_type = {},strength=1, constitution=2, dexterity=3, intelligence=6, wisdom=4, charisma=5)
    actual = race_to_dict(race)
    assert expected == actual

def test_case():
    expected = Race("Human", "George", 1, 1, strength=1, constitution=1, dexterity=1, intelligence=1, charisma=1, wisdom=1, body_type = {
            "Main Hand": "Nothing",
            "Off Hand": "Nothing",
            "Head": "Nothing",
            "Neck": "Nothing",
            "Body" : "Nothing",
            "Back" : "Nothing",
            "Waist": "Nothing",
            "Hands" : "Nothing",
            "Feet": "Nothing",
            "Ring Slot 1": "Nothing",
            "Ring Slot 2": "Nothing",
        "Bag Slot": "Nothing"
        })
    actual = race_from_dict(race_to_dict(expected))
    assert expected == actual