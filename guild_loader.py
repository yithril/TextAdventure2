import json
from glob import glob
from json import JSONDecodeError

import logging

from guild import Guild

"""
Should return guild object or raise an error
"""

logger = logging.getLogger()


def class_skill_cost_from_dict(cost):
    base = {
        "Appraise": 2,
        "Climb": 2,
        "Craft Potion": 2,
        "Craft Spell": 2,
        "Craft Weapon": 2,
        "Craft Armor": 2,
        "Deciper Script": 2,
        "Diplomacy": 2,
        "Heal": 2,
        "Jump": 2,
        "Open Lock": 2,
        "Move Silently": 2,
        "Swim": 2,
        "Perception": 2,
        "Use Magic Device": 2
    }
    base.update(cost)
    return base


def guild_from_dict(dict):
    name = dict['name']
    desc = dict['desc']
    bab_modifier = dict['bab_modifier']
    fort_save = dict['fort_save']
    will_save = dict['will_save']
    ref_save = dict['ref_save']
    equipment_type = dict['equipment_type']
    hit_dice = dict['hit_dice']
    mana_modifier = dict['mana_modifier']
    allowed_weapon_types = dict['allowed_weapon_types']
    main_stat = dict['main_stat']
    skill_points = dict['skill_points']
    class_skill_cost = dict.get("class_skill_cost", {})
    class_skill_cost = class_skill_cost_from_dict(class_skill_cost)
    return Guild(name, desc, bab_modifier, fort_save, will_save, ref_save, equipment_type, hit_dice, mana_modifier, class_skill_cost, allowed_weapon_types, main_stat, skill_points)


def guild_to_dict(guild):
    guild.get_name()
    return {"name" : guild.get_name(), "desc": guild.get_desc(), "bab_modifier" : guild.get_bab_modifier(), "fort_save" : guild.get_fort_save(), "will_save" : guild.get_will_save(), "ref_save": guild.get_reflex_save(), "equipment_type": guild.get_equipment_type(), "hit_dice": guild.get_hit_dice(), "mana_modifier": guild.get_mana_modifier(), "class_skill_costs": guild.get_class_skill_cost()}


def load_guild_from_file(path = "data/guilds/wizard.json"):
    try:
        with open(path) as json_data:
            d = json.load(json_data)
            return guild_from_dict(d)
    except (JSONDecodeError, ValueError) as e:
        logger.error("Failed to load guild file: %s, reason: %s", path, e)
        raise e

def load_guilds():
    files = glob("data/guilds/*.json")
    result = [load_guild_from_file(path) for path in files]
    return result