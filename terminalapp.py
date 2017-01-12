from Action_repository import ActionRepo
from Game_State import Game_State
from actions.move import MoveAction
from actions.look import LookAction
from actions.take import TakeItemAction
from actions.drop import DropItemAction
from caching_repository import Caching_Repository
from factory import Room_Factory
from file_loader import File_Loader
from repository import Repository



class TerminalApp:

    def __init__(self, action_repository):
        self.game_state = Game_State(1, player = AnonPlayer())
        self.action_repository = action_repository

    def process(self,line):
        action_name, arg = line.split(' ', 1)
        action = self.action_repository.get_by_name(action_name)
        if action is None:
            print("WTF is", action_name)
        else:
            action.do(arg)



if __name__ == '__main__':
    room_path = "data/rooms/"
    room_loader = File_Loader(room_path)
    room_repo = Caching_Repository(Repository(room_loader, Room_Factory))
    action_repo = ActionRepo()
    action_repo.add("move", MoveAction(room_repo))
    action_repo.add("look", LookAction(room_repo))
    action_repo.add("take", TakeItemAction(room_repo))
    action_repo.add("drop", DropItemAction(room_repo))
    app = TerminalApp(action_repo)

    line = input("Do>")
    while line:
        app.process((line))