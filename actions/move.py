class MoveAction:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def do(self, state, direction):
        state.room_id = self.room_repository.get_by_id(state.room_id).neighbors.get(direction, state.room_id)