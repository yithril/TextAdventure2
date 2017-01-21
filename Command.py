import cmd
import textwrap

from Action_repository import ActionRepo
from Character import Character
from Game_State import Game_State
from actions.gold import Gold
from actions.inventory import Inventory
from actions.limbs import LimbsAction
from actions.move import MoveAction
from actions.look import LookAction
from actions.status import StatusAction
from actions.take import TakeItemAction
from actions.drop import DropItemAction
from actions.unwield import UnwieldAction
from actions.wear import WearArmorAction
from actions.wield import WieldAction
from actions.remove import RemoveAction
from caching_repository import Caching_Repository
from factory import Room_Factory
from file_loader import File_Loader
from guild_loader import load_guild_from_file
from race_loader import load_race_from_file
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

    def do_e(self, args):
        """Just type 'e' to move east."""
        action_repo.get_by_name("move").do(self.game_state, "e")
        action_repo.get_by_name("look").do(self.game_state, None)

    def do_w(self, args):
        """Just type 'w' to move west."""
        action_repo.get_by_name("move").do(self.game_state, "w")
        action_repo.get_by_name("look").do(self.game_state, None)

    def do_s(self, args):
        """Just type 's' to move south."""
        action_repo.get_by_name("move").do(self.game_state, "s")
        action_repo.get_by_name("look").do(self.game_state, None)

    def do_n(self, args):
        """Just type 'n' to move north."""
        action_repo.get_by_name("move").do(self.game_state, "n")
        action_repo.get_by_name("look").do(self.game_state, None)

    def do_take(self, itemname):
        """Syntax: take <item>"""
        action_repo.get_by_name("take").do(self.game_state, itemname)

    def do_wield(self, itemname):
        """Wield <weapon> will default to your main hand.  Wield <weapon> offhand will wield the weapon in your off hand if your character is capable."""
        action_repo.get_by_name("wield").do(self.game_state,itemname)

    def do_unwield(self,itemname):
        """Unwield <weapon> to unwield a weapon."""
        action_repo.get_by_name("unwield").do(self.game_state, itemname)

    def do_wear(self, itemname):
        """Wear <armor> will attempt to wear a piece of armor or a shield."""
        action_repo.get_by_name("wear").do(self.game_state, itemname)

    def do_remove(self, itemname):
        """Remove <armor> will attempt to remove a piece of armor you are currently wearing."""
        action_repo.get_by_name("remove").do(self.game_state, itemname)

    def do_drop(self, itemname):
        """Syntax: drop <item>"""
        action_repo.get_by_name("drop").do(self.game_state, itemname)

    def do_inventory(self, args):
        """Displays player inventory."""
        action_repo.get_by_name("inventory").do(self.game_state)

    def do_gold(self, args):
        """Displays the amount of gold you possess."""
        action_repo.get_by_name("gold").do(self.game_state)

    def do_status(self,args):
        """Displays the current HP, MP, Experience, and Encumbrance of your character."""
        action_repo.get_by_name("status").do(self.game_state)

    def do_limbs(self,args):
        """Display all equipment slots and what weapons and armor you currently have equipped."""
        action_repo.get_by_name("limbs").do(self.game_state)

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
    path = "data/races/half-elf.json"
    player_race = load_race_from_file(path)
    path2 = "data/guilds/paladin.json"
    player_guild = load_guild_from_file(path2)
    action_repo = ActionRepo()
    action_repo.add("move", MoveAction(room_repo))
    action_repo.add("look", LookAction(room_repo, npc_repo, item_repo))
    action_repo.add("take", TakeItemAction(room_repo, item_repo))
    action_repo.add("drop", DropItemAction(room_repo, item_repo))
    action_repo.add("inventory", Inventory(item_repo))
    action_repo.add("wield", WieldAction(item_repo))
    action_repo.add("wear", WearArmorAction(item_repo))
    action_repo.add("remove", RemoveAction(item_repo))
    action_repo.add("unwield", UnwieldAction(item_repo))
    action_repo.add("status", StatusAction())
    action_repo.add("limbs", LimbsAction(item_repo))
    action_repo.add("gold", Gold())
    player = Character("Character", "George", [], description = "A player", keywords = [], race = player_race, sex = "Male", guild = player_guild, ac = 10, mp = 10, hp = 10, strength = 10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10, level=1, gold=100, xp=0, encumbrance=0, feats=[])
    g = Game()
    g.cmdloop()