import cmd
import textwrap

from Action_repository import ActionRepo
from Character import Character
from Game_State import Game_State
from actions.gold import Gold
from actions.inventory import Inventory
from actions.move import MoveAction
from actions.look import LookAction
from actions.take import TakeItemAction
from actions.drop import DropItemAction
from caching_repository import Caching_Repository
from factory import Room_Factory
from file_loader import File_Loader
from repository import Repository
from factory import Character_Factory
from factory import Item_Factory


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.game_state = Game_State(1, player)
        self.do_look(None)
        self.prompt = '>>'


    def do_look(self,dir):
        """Syntax: Look, Look <direction>, or Look <item or npc>"""
        action_repo.get_by_name("look").do(self.game_state, dir)


    def do_move(self, dir):
        """Syntax move <direction>.  Valid directions are listed in exits."""
        if not dir:
            print("You must input a direction to move in,")
        else:
            action_repo.get_by_name("move").do(self.game_state,dir)
            action_repo.get_by_name("look").do(self.game_state, None)


    def do_take(self, itemname):
        """Syntax: take <item>"""
        action_repo.get_by_name("take").do(self.game_state, itemname)


    def do_drop(self, itemname):
        """Syntax: drop <item>"""
        action_repo.get_by_name("drop").do(self.game_state, itemname)

    def do_inventory(self, args):
        """Displays player inventory."""
        action_repo.get_by_name("inventory").do(self.game_state)

    def do_gold(self, args):
        action_repo.get_by_name("gold").do(self.game_state)

    def do_status(self,args):
        pass

    def do_quit(self, args):
        print("Thanks for playing!")
        return -1

if __name__ == "__main__":
    room_path = "data/rooms/"
    room_loader = File_Loader(room_path)
    room_repo = Caching_Repository(Repository(room_loader, Room_Factory))
    npc_path = "data/npc/"
    npc_loader = File_Loader(npc_path)
    npc_repo = Caching_Repository(Repository(npc_loader, Character_Factory))
    item_path = "data/items/"
    item_loader = File_Loader(item_path)
    item_repo = Caching_Repository(Repository(item_loader, Item_Factory))
    action_repo = ActionRepo()
    action_repo.add("move", MoveAction(room_repo))
    action_repo.add("look", LookAction(room_repo, npc_repo, item_repo))
    action_repo.add("take", TakeItemAction(room_repo, item_repo))
    action_repo.add("drop", DropItemAction(room_repo, item_repo))
    action_repo.add("inventory", Inventory(item_repo))
    action_repo.add("gold", Gold())
    player = Character("Character", "George", [], description = "A player", keywords = [], race = "Human", sex = "Male", guild = "Paladin", ac = 10, mp = 10, hp = 10, strength = 10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10, level=1, gold=100, xp=0, encumbrance=0, feats=[])
    g = Game()
    g.cmdloop()