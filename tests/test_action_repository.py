import pytest
from actions.move import MoveAction
from caching_repository import Caching_Repository
from factory import Room_Factory
from file_loader import File_Loader
from repository import Repository

class ActionRepo(object):
    def __init__(self, cache = {}):
        self._cache = cache

    def get_cache(self):
        return self._cache

    def add(self,name,action):
        path = "actions/"
        if action not in self._cache:
            self._cache[name] = action
        return self._cache[name]

    def get_by_name(self,name):
        return self._cache[name]




def test_add_action():
    action_repo = ActionRepo()
    room_path = "data/rooms/"
    room_loader = File_Loader(room_path)
    room_repo = Caching_Repository(Repository(room_loader, Room_Factory))
    action_repo.add("move", MoveAction(room_repo))
    action_repo.add("move", MoveAction(room_repo))
    assert len(action_repo.get_cache()) == 1
    action_repo.add("look",  MoveAction(room_repo))
    action_repo.add("jump",  MoveAction(room_repo))
    assert len(action_repo.get_cache()) == 3
    action_repo.add("look", MoveAction(room_repo))
    assert len(action_repo.get_cache()) == 3

def test_get_by_name():
    action_repo = ActionRepo()
    room_path = "data/rooms/"
    room_loader = File_Loader(room_path)
    room_repo = Caching_Repository(Repository(room_loader, Room_Factory))
    action_repo.add("move", MoveAction(room_repo))
    assert action_repo.get_by_name("move") is not None

