import pytest

from room import Room



test_room1 = Room(id = 1, name = "A room", description = "description", neighbors= {"e": "room"}, npc_inv=[], items_inv =[], indoors = True, terrain = "Room")
test_room2 = Room(id = 2, name = "A room is here", description = "description is longer", neighbors= {"w": "a different room"}, npc_inv=[], items_inv =[], indoors = True, terrain = "Room")


def test_room_is_not_none():
    return test_room1 is not None

def test_room_has_neighbors():
    assert test_room1.neighbors is not None
    assert test_room1.neighbor("e") is not None
    assert test_room1.neighbor("w") is None
    assert test_room1.neighbor("Superman") is None

