from Game_Screen import Game_Screen


class LookAction:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def do(self, state, direction):
        message = ""
        room = self.room_repository.get_by_id(state.room_id)
        if not direction or direction == "here":
            message += room.get_name()
            message += room.get_description()
            message += room.get_room_npc_description()
            message += room.get_item_description()
        elif not room.neighbor(direction):
            message += "You cannot look in that direction."
        else:
            room2 = self.room_repository.get_by_id(room.neighbor(direction))
            message += room2.get_name()
            message += room2.get_description()
            message += room.get_room_npc_description()
            message += room.get_item_description()
        Game_Screen(message)





