from Game_Screen import Game_Screen


class LookAction:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def do(self, state, direction):
        room = self.room_repository.get_by_id(state.room_id)
        if not direction or direction == "here":
            print(room.get_description())
        elif not room.neighbor(direction):
            print("There isn't anything in that direction.")
        else:
            room2 = self.room_repository.get_by_id(room.neighbor(direction))
            print(room2.get_description())








