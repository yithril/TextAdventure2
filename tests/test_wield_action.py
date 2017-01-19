import pytest

from Game_State import Game_State
from Weapon import Weapon
from items import Items


class MockRepository:
    def __init__(self, *args):
        self._repo = dict((e.get_id(), e) for e in args)

    def get_by_id(self, id):
        return self._repo[id]

@pytest.fixture()
def item_repository():
    return MockRepository(Weapon(id = 1, name = "longsword", desc = "a rock", long_desc = "a rock", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = ["longsword"], type = "Weapon", handed=1, offhand = 0, weapon_type = "sword", const_damage = 1, damage_hit_dice = 4, damage_hit_dice_coefficient=1, damage_stat="dexterity", damage_type="slashing"),
    Weapon(id = 2, name = "silver longsword", desc = "a rock", long_desc = "a rock", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = ["pebble"], type = "Weapon", handed=1, offhand = 0, weapon_type = "sword", const_damage = 1, damage_hit_dice = 4, damage_hit_dice_coefficient=1, damage_stat="dexterity", damage_type="slashing"),Items(id=3, name="pebble", desc="a rock", long_desc="a feather", weight=1, value=1,
                                can_pick_up="True", is_magical="True", is_cursed="False", keywords=["longsword"], type="Item", material = "stone"))


class MockPlayer():
    def __init__(self, inventory):
        self.inventory = inventory

class WieldAction():
    def __init__(self,item_repository):
        self.item_repository = item_repository

    def do(self,state,itemname):
        player = state.player
        if not itemname:
            print("Wield what?")
            return
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                #Is it a weapon
                if item.get_type() is not "Weapon":
                    print("That cannot be wielded.")
                    return
                #Does your class allow you to wield this?
                if item.get_type() not in player.guild.get_equipment_type():
                    print("{0}s are not allowed to wield {1}s".format(player.guild.get_name(), item.get_weapon_type()))
                #Check if main hand is empty.  Main hand is always checked first.
                if player.race.get_body_slot("Main Hand") == "Nothing":
                    player.race.set_body_slot("Main Hand", item.get_id())
                    print("You wield the",item.get_name())
                    return
                #Two weapon fighting feet for offhand and offhand is empty
                elif "Two Weapon Fighting" in player.get_feats() and player.race.get_body_slot("Off Hand") == "Nothing":
                    player.race.set_body_slot("Off Hand", item.get_id())
                    print("You wield the",item.get_name())
                    return
                elif "Two Weapon Fighting" not in player.get_feats():
                    print("You do not know how to dual wield.")
                    return
                else:
                    print("You are already wielding something in your off hand.")
                    return


@pytest.fixture()
def state():
    return Game_State(1, player = MockPlayer(inventory = [1,2, 3]))

@pytest.fixture()
def wieldaction(item_repository):
    return WieldAction(item_repository)

def test_item_can_be_wielded(item_repository):
    wieldaction.do(state, "rock")

