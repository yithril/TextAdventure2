import pytest

from Game_State import Game_State
from room import Room


class MockRepository:
    def __init__(self, *args):
        self._repo = dict((e.get_id(), e) for e in args)

    def get_by_id(self, id):
        return self._repo[id]

@pytest.fixture()
def room_repository():
    return MockRepository(Room(id = 1, name = "A room", description = "description", neighbors= {"e": 2}, npc_inv=[], items_inv ={
        "rock":1
    }, indoors = True, terrain = "Room"),
                          Room(id = 2, name = "A room is here",
                               description = "description is longer", neighbors= {"w": 1}, npc_inv=[], items_inv ={}, indoors = True, terrain = "Room")
                          )

class TakeItemAction():
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def do(self, state, itemname):
        room = self.room_repository.get_by_id(state.room_id)
        player = state.player
        if itemname in room._items_inv:
            player.inventory[itemname] = room._items_inv[itemname]
            del room._items_inv[itemname]

class MockPlayer():
    def __init__(self):
        self.inventory = {}

@pytest.fixture()
def state():
    return Game_State(1, player = MockPlayer())


@pytest.fixture()
def takeaction(room_repository):
    return TakeItemAction(room_repository)

def test_take_item(state,takeaction, room_repository):
    room = room_repository.get_by_id(state.room_id)
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 1
    takeaction.do(state, itemname = "rock")
    assert len(state.player.inventory) == 1
    assert len(room._items_inv) == 0

def test_take_item_nonexistant(state, takeaction, room_repository):
    room = room_repository.get_by_id(state.room_id)
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 1
    takeaction.do(state, itemname = "Bob")
    assert len(state.player.inventory) == 0
    assert len(room._items_inv) == 1
