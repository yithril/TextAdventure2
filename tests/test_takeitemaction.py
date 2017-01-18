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
    return MockRepository(Items(id = 1, name = "rock", desc = "a rock", long_desc = "a rock", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = ["pebble"], type = "Item"),
                          Items(id=2, name="pebble", desc="a rock", long_desc="a feather", weight=1, value=1,
                                can_pick_up="True", is_magical="True", is_cursed="False", keywords=["plume"], type="Item"),)

@pytest.fixture()
def room_repository():
    return MockRepository(Room(id = 1, name = "A room", description = "description", neighbors= {"e": 2}, npc_inv=[], items_inv =[1], indoors = True, terrain = "Room", lighting = 100, room_description = {}),
                          Room(id = 2, name = "A room is here",
                               description = "description is longer", neighbors= {"w": 1}, npc_inv=[], items_inv ={}, indoors = True, terrain = "Room", lighting = 100, room_description = {}),
    Room(id=3, name="A room is here", description="description is longer", neighbors={"w": 1}, npc_inv=[], items_inv={1,2}, indoors=True, terrain="Room", lighting=100, room_description={})
                          )


class TakeItemAction():
    def __init__(self, room_repository, item_repository):
        self.room_repository = room_repository
        self.item_repository = item_repository

    def do(self, state, itemname):
        room = self.room_repository.get_by_id(state.room_id)
        player = state.player
        for itemid in room.get_item_ids():
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                player.inventory.append(item.get_id())
                room.remove_item(item.get_id())
                return
        for itemid in room.get_item_ids():
            item = self.item_repository.get_by_id(itemid)
            if itemname in item.get_keywords():
                player.inventory.append(item.get_id())
                room.remove_item(item.get_id())
                return
        return

class MockPlayer():
    def __init__(self):
        self.inventory = []

@pytest.fixture()
def state():
    return Game_State(1, player = MockPlayer())


@pytest.fixture()
def takeaction(room_repository, item_repository):
    return TakeItemAction(room_repository, item_repository)

def test_take_item(state,takeaction, room_repository, item_repository):
    room = room_repository.get_by_id(state.room_id)
    item = map(item_repository.get_by_id, room.get_item_ids())
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 1
    takeaction.do(state, itemname = "rock")
    assert len(state.player.inventory) == 1
    assert len(room._items_inv) == 0

def test_take_item_from_room_with_many_things(state, takeaction, room_repository, item_repository):
    state.room_id = 3
    room = room_repository.get_by_id(3)
    item = map(item_repository.get_by_id, room.get_item_ids())
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 2
    assert state.room_id == 3
    takeaction.do(state, itemname="rock")
    assert len(state.player.inventory) == 1
    assert len(room._items_inv) == 1


def test_take_item_nonexistant(state, takeaction, room_repository):
    room = room_repository.get_by_id(state.room_id)
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 1
    takeaction.do(state, itemname = "Bob")
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 1

def test_takeitems_from_keywords(state,takeaction, room_repository, item_repository):
    state.room_id = 3
    room = room_repository.get_by_id(state.room_id)
    item = map(item_repository.get_by_id, room.get_item_ids())
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 2
    takeaction.do(state, itemname="pebble")
    assert len(state.player.inventory) == 1
    assert len(room._items_inv) == 1
    assert 2 in state.player.inventory
    assert 1 in room.get_item_ids()

def test_take_item_using_keyword(state,takeaction,room_repository):
    rock = Items(id = 1, name = "rock", desc = "a rock", long_desc = "a rock", weight = 1, value = 1, can_pick_up = "True", is_magical = "True", is_cursed = "False", keywords = [], type = "Item")
    room = room_repository.get_by_id(state.room_id)
    takeaction.do(state, itemname = "rock")

