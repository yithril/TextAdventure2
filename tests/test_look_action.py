import pytest

from Game_Screen import Game_Screen
from Game_State import Game_State
from room import Room

class MockRepository:
    def __init__(self, *args):
        self._repo = dict((e.get_id(), e) for e in args)

    def get_by_id(self, id):
        return self._repo[id]

class MockRepository2:
    def __init__(self,*args):
        pass

@pytest.fixture()
def room_repository():
    return MockRepository(Room(id = 1, name = "A room", description = "description", neighbors= {"e": 2}, npc_inv=[], items_inv ={
        "rock":1
    }, indoors = True, terrain = "Room", lighting = 80, room_description={}),
                          Room(id = 2, name = "A room is here",
                               description = "description is longer", neighbors= {"w": 1}, npc_inv=[], items_inv ={}, indoors = True, terrain = "Room", lighting = 80, room_description={})
                          )

class MockPlayer():
    def __init__(self):
        self.inventory = {}

@pytest.fixture()
def state():
    return Game_State(1, player = MockPlayer())

@pytest.fixture()
def look_action(room_repository):
    return LookAction(room_repository)

class LookAction:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def do(self, state, direction):
        message = ""
        room = self.room_repository.get_by_id(state.room_id)
        if not direction or direction == "here":
            message += room.get_name()+"/n"
            message += room.get_description()+"/n"
            message += room.get_room_npc_list()+"/n"
            message += room.get_room_item_list()
        elif not room.neighbor(direction):
            message += "You cannot look in that direction."
        else:
            room2 = self.room_repository.get_by_id(room.neighbor(direction))
            message += room2.get_name() + "/n"
            message += room2.get_description() + "/n"
            message += room2.get_room_npc_list() + "/n"
            message += room2.get_room_item_list()
        Game_Screen(message)

def test_look_action(state, room_repository, look_action):
    room = room_repository.get_by_id(state.room_id)
    comparison = room.get_id()
    look_action.do(state, "n")
    assert room.get_id() == comparison



