import pytest

from Armor import Armor
from Game_State import Game_State
from guild_loader import load_guild_from_file
from items import Items
from race_loader import load_race_from_file


class MockRepository:
    def __init__(self, *args):
        self._repo = dict((e.get_id(), e) for e in args)

    def get_by_id(self, id):
        return self._repo[id]

class MockPlayer():
    def __init__(self, inventory, race, guild):
        self.inventory = inventory
        self.race = race
        self.guild = guild


@pytest.fixture()
def item_repository():
    return MockRepository(Armor(id = 1, name = "Chain Shirt", desc = "a chainmail shirt", long_desc = "a rugged chainmail shirt", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = ["shirt"], type = "Armor", material = "iron", armor_ac = 2, armor_level = 2, slot = "Body", max_dex_bonus = 2),
                          Armor(id=2, name="Iron Helmet", desc="a chainmail shirt",
                                long_desc="a rugged chainmail shirt", weight=1, value=1, can_pick_up="True",
                                is_magical="True", is_cursed="False", keywords=["helmet"], type="Armor",
                                material="iron", armor_ac=2, armor_level=0, slot= "Head", max_dex_bonus=2), Items(id = 3, name = "rock", desc = "a rock", long_desc = "a rock", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = [], type = "Item", material = "stone"),Armor(id=4, name="helmet", desc="a chainmail shirt",
                                long_desc="a rugged chainmail shirt", weight=1, value=1, can_pick_up="True",
                                is_magical="True", is_cursed="False", keywords=["mask"], type="Armor",
                                material="iron", armor_ac=2, armor_level=0, slot= "Head", max_dex_bonus=2), Armor(id=5, name="iron ring", desc="a chainmail shirt",
                                long_desc="a rugged chainmail shirt", weight=1, value=1, can_pick_up="True",
                                is_magical="True", is_cursed="False", keywords=["ring"], type="Armor",
                                material="iron", armor_ac=2, armor_level=0, slot= "Ring", max_dex_bonus=2),Armor(id=6, name="gold ring", desc="a chainmail shirt",
                                long_desc="a rugged chainmail shirt", weight=1, value=1, can_pick_up="True",
                                is_magical="True", is_cursed="False", keywords=["ring"], type="Armor",
                                material="iron", armor_ac=2, armor_level=0, slot= "Ring", max_dex_bonus=2), Armor(id=7, name="skeleton ring", desc="a chainmail shirt",
                                long_desc="a rugged chainmail shirt", weight=1, value=1, can_pick_up="True",
                                is_magical="True", is_cursed="False", keywords=["ring"], type="Armor",
                                material="iron", armor_ac=2, armor_level=0, slot= "Ring", max_dex_bonus=2))

@pytest.fixture()
def state():
    path = "data/races/half-elf.json"
    race = load_race_from_file(path)
    path2 = "data/guilds/wizard.json"
    guild = load_guild_from_file(path2)
    inventory = [1,2,3]
    return Game_State(1, player = MockPlayer(inventory, race, guild))

@pytest.fixture()
def wearaction(item_repository):
    return WearArmorAction(item_repository)


class WearArmorAction:
    def __init__(self, item_repository):
        self.item_repository = item_repository

    def do(self, state, itemname):
        player = state.player
        dictionary = player.race.get_body_type()
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                #Only Armor can be worn
                    if item.get_type() is not "Armor":
                        print("That cannot be worn.")
                        return
                    elif item.get_armor_level() > player.guild.get_equipment_type():
                        print("That armor is too cumbersome for {0}s to wear.".format(player.guild.get_name()))
                        return
                    elif item.get_armor_slot() == "Ring":
                        if player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is not 0:
                            print("Both your ring slots are full.")
                            return
                        elif player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is 0:
                            player.race.set_body_slot("Ring Slot 2", item.get_id())
                            print("You wear the {0} in your second ring slot.".format(item.get_name()))
                            return
                        else:
                            player.race.set_body_slot("Ring Slot 1", item.get_id())
                            print("You wear the {0}".format(item.get_name()))
                            return
                    elif player.race.get_body_slot(item.get_armor_slot()) is not 0:
                        print("You are already wearing something in your {0} slot.".format(item.get_armor_slot().lower()))
                        return
                    else:
                        player.race.set_body_slot(item.get_armor_slot(), item.get_id())
                        print("You wear the {0}".format(item.get_name()))
                        return
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname in item.get_keywords():
                #Only Armor can be worn
                    if item.get_type() is not "Armor":
                        print("That cannot be worn.")
                        return
                    elif item.get_armor_level() > player.guild.get_equipment_type():
                        print("That armor is too cumbersome for {0}s to wear.".format(player.guild.get_name()))
                        return
                    elif item.get_armor_slot() == "Ring":
                        if player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is not 0:
                            print("Both your ring slots are full.")
                            return
                        elif player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is 0:
                            player.race.set_body_slot("Ring Slot 2", item.get_id())
                            print("You wear the {0} in your second ring slot.".format(item.get_name()))
                            return
                        else:
                            player.race.set_body_slot("Ring Slot 1", item.get_id())
                            print("You wear the {0}".format(item.get_name()))
                            return
                    elif player.race.get_body_slot(item.get_armor_slot()) is not 0:
                        print("You are already wearing something in your {0} slot.".format(item.get_armor_slot().lower()))
                        return
                    else:
                        player.race.set_body_slot(item.get_armor_slot(), item.get_id())
                        print("You wear the {0}".format(item.get_name()))
                        return


def test_only_wear_armor(state, wearaction, item_repository):
    player = state.player
    rock = Items(id = 3, name = "rock", desc = "a rock", long_desc = "a rock", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = [], type = "Item", material = "stone")
    dictionary = player.race.get_body_type()
    for key in dictionary:
        assert dictionary[key] == 0
    wearaction.do(state, itemname = "rock")
    for key in dictionary:
        assert dictionary[key] == 0

def test_class_can_wear_armor(state, wearaction, item_repository):
    player = state.player
    dictionary = player.race.get_body_type()
    for key in dictionary:
        assert dictionary[key] == 0
    wearaction.do(state, itemname = "Chain Shirt")
    for key in dictionary:
        assert dictionary[key] == 0

def test_already_in_slot(state,wearaction):
    player = state.player
    dictionary = player.race.get_body_type()
    player.race.set_body_slot("Head", 1)
    wearaction.do(state, itemname = "Iron Helmet")
    assert dictionary["Head"] == 1
    assert dictionary["Body"] == 0
    assert dictionary["Neck"] == 0
    assert dictionary["Back"] == 0
    assert dictionary["Waist"] == 0
    assert dictionary["Hands"] == 0
    assert dictionary["Feet"] == 0
    assert dictionary["Ring Slot 1"] == 0
    assert dictionary["Ring Slot 2"] == 0
    assert dictionary["Bag Slot"] == 0

def test_wear_success(state, wearaction):
    player = state.player
    dictionary = player.race.get_body_type()
    for key in dictionary:
        assert dictionary[key] == 0
    wearaction.do(state, itemname="Iron Helmet")
    dictionary = player.race.get_body_type()
    assert dictionary["Head"] == 2

def test_wear_checks_name_first(state, wearaction):
    player = state.player
    player.inventory = [2,4]
    dictionary = player.race.get_body_type()
    for key in dictionary:
        assert dictionary[key] == 0
    wearaction.do(state, itemname="helmet")
    dictionary = player.race.get_body_type()
    assert dictionary["Head"] == 4

def test_ring_wear(state, wearaction):
    player = state.player
    player.inventory = [5,6,7]
    dictionary = player.race.get_body_type()
    for key in dictionary:
        assert dictionary[key] == 0
    wearaction.do(state, itemname="iron ring")
    dictionary = player.race.get_body_type()
    assert dictionary["Ring Slot 1"]== 5
    wearaction.do(state, itemname="gold ring")
    dictionary = player.race.get_body_type()
    assert dictionary["Ring Slot 2"] == 6
    wearaction.do(state, itemname="skeleton ring")
    assert dictionary["Ring Slot 1"] == 5
    assert dictionary["Ring Slot 2"] == 6









