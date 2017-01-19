import pytest

from Game_State import Game_State
from items import Items
from room import Room


class MockRepository:
    def __init__(self, *args):
        self._repo = dict((e.get_id(), e) for e in args)

    def get_by_id(self, id):
        return self._repo[id]

@pytest.fixture()
def item_repository():
    return MockRepository(Items(id = 1, name = "rock", desc = "a rock", long_desc = "a rock", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = ["pebble"], type = "Item", material = "stone"),
                          Items(id=2, name="pebble", desc="a rock", long_desc="a feather", weight=1, value=1,
                                can_pick_up="True", is_magical="True", is_cursed="False", keywords=["plume"], type="Item", material = "stone"),)

@pytest.fixture()
def room_repository():
    return MockRepository(Room(id = 1, name = "A room", description = "description", neighbors= {"e": 2}, npc_inv=[], items_inv =[], indoors = True, terrain = "Room", lighting = 100, room_description = {}),
                          Room(id = 2, name = "A room is here",
                               description = "description is longer", neighbors= {"w": 1}, npc_inv=[], items_inv =[], indoors = True, terrain = "Room", lighting = 100, room_description = {}),
    Room(id=3, name="A room is here", description="description is longer", neighbors={"w": 1}, npc_inv=[], items_inv=[], indoors=True, terrain="Room", lighting=100, room_description={})
                          )

class DropItemAction():
    def __init__(self, room_repository, item_repository):
        self.room_repository = room_repository
        self.item_repository = item_repository

    def do(self, state, itemname):
        room = self.room_repository.get_by_id(state.room_id)
        player = state.player
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                print("You drop ",item.get_name())
                room.add_item(item.get_id())
                player.inventory.remove(item.get_id())
                return
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname in item.get_keywords():
                print("You drop ", item.get_name())
                room.add_item(item.get_id)
                player.inventory.remove(item.get_id())
                return

class MockPlayer():
    def __init__(self, inventory):
        self.inventory = inventory

@pytest.fixture()
def state():
    return Game_State(1, player = MockPlayer(inventory = [1,2]))


@pytest.fixture()
def dropaction(room_repository, item_repository):
    return DropItemAction(room_repository, item_repository)

def test_drop_item(state, dropaction, room_repository, item_repository):
    room = room_repository.get_by_id(state.room_id)
    item = map(item_repository.get_by_id, room.get_item_ids())
    assert len(state.player.inventory) == 2
    assert len(room._items_inv) == 0
    dropaction.do(state, itemname = "rock")
    assert len(state.player.inventory) == 1
    assert len(room._items_inv) == 1

def test_drop_item_nonexistant(state, dropaction, room_repository, item_repository):
    room = room_repository.get_by_id(state.room_id)
    item = map(item_repository.get_by_id, room.get_item_ids())
    assert len(state.player.inventory) == 2
    assert len(room._items_inv) == 0
    dropaction.do(state, itemname = "Bob")
    assert len(state.player.inventory) == 2
    assert len(room._items_inv) == 0

def test_drop_by_name_first_then_keywords(state, dropaction, room_repository, item_repository):
    state.room_id = 3
    room = room_repository.get_by_id(state.room_id)
    item = map(item_repository.get_by_id, room.get_item_ids())
    assert len(state.player.inventory) == 2
    assert len(room._items_inv) == 0
    dropaction.do(state, itemname="pebble")
    assert len(state.player.inventory) == 1
    assert len(room._items_inv) == 1


