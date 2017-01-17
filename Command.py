import cmd
import textwrap

from Action_repository import ActionRepo
from Character import Character
from Game_State import Game_State
from actions.move import MoveAction
from actions.look import LookAction
from actions.take import TakeItemAction
from actions.drop import DropItemAction
from caching_repository import Caching_Repository
from factory import Room_Factory
from file_loader import File_Loader
from repository import Repository


class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.game_state = Game_State(1, player)
        self.prompt = '>>'

    def do_look(self,dir):
        action_repo.get_by_name("move").do(self.game_state, dir)

    def do_move(self, dir):
        if not dir:
            print("You must input a direction to move in,")
        else:
            action_repo.get_by_name("move").do(self.game_state,dir)

    def do_take(self, itemname):
        action_repo.get_by_name("take").do(self.game_state, itemname)

    def do_quit(self):
        print("Thanks for playing!")
        return True


if __name__ == "__main__":
    room_path = "data/rooms/"
    room_loader = File_Loader(room_path)
    room_repo = Caching_Repository(Repository(room_loader, Room_Factory))
    action_repo = ActionRepo()
    action_repo.add("move", MoveAction(room_repo))
    action_repo.add("look", LookAction(room_repo))
    action_repo.add("take", TakeItemAction(room_repo))
    action_repo.add("drop", DropItemAction(room_repo))
    player = Character("George", [])
    g = Game()
    g.cmdloop()