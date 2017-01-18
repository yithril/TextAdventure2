import pytest

from Game_State import Game_State
from actions.look import LookAction
from actions.move import MoveAction
from room import Room


class MockRepository:
    def __init__(self, *args):
        self._repo = dict((e.get_id(), e) for e in args)

    def get_by_id(self, id):
        return self._repo[id]

@pytest.fixture()
def room_repository():
    return MockRepository(Room(id = 1, name = "A room", description = "description", neighbors= {"e": 2}, npc_inv=[], items_inv =[], indoors = True, terrain = "Room", lighting = 100, room_description = {}),
                          Room(id = 2, name = "A room is here",
                               description = "description is longer", neighbors= {"w": 1}, npc_inv=[], items_inv =[], indoors = True, terrain = "Room", lighting = 100, room_description = {})
                          )

@pytest.fixture()
def state():
    return Game_State(1)


@pytest.fixture()
def moveaction(room_repository):
    return MoveAction(room_repository)

@pytest.fixture()
def lookaction(room_repository):
    return LookAction(room_repository)


@pytest.mark.parametrize("directions,end_room_id",
                         [
                             (["Superman"], 1),
                             (["e"],2),
                             (['e','w'],1)
                         ]
                         )
def test_move(state,moveaction,directions,end_room_id):
    assert state.room_id == 1
    for direction in directions:
        moveaction.do(state, direction)
    assert state.room_id == end_room_id

@pytest.mark.parametrize("directions,start_room_id",
                         [
                             (["Superman"], 1),
                             (["e"],1),
                             (['e','w'],1)
                         ]
                         )
def test_look(state,lookaction,directions,start_room_id):
    assert state.room_id == 1
    for direction in directions:
        lookaction.do(state, direction)
    assert state.room_id == start_room_id





