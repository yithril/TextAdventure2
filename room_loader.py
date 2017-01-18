from caching_repository import Caching_Repository
from factory import Character_Factory, Room_Factory
from factory import Item_Factory
from file_loader import File_Loader
from repository import Repository

npc_path = "data/npc/"
npc_loader = File_Loader(npc_path)
npc_repo = Caching_Repository(Repository(npc_loader, Character_Factory))

class Room_Loader(object):

    def load_npcs(self, npcs):
        npc_list = []
        for npc in npcs:
            npc = npc_repo.get_by_id(npc)
            npc_list.append(npc)
        return npc_list

