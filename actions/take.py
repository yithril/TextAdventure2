class TakeItemAction:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def do(self, state, itemname):
        room = self.room_repository.get_by_id(state.room_id)
        player = state.player
        if itemname in room._items_inv:
            player.inventory[itemname] = room._items_inv[itemname]
            del room._items_inv[itemname]