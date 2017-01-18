class DropItemAction():
    def __init__(self, room_repository, item_repository):
        self.room_repository = room_repository
        self.item_repository = item_repository

    def do(self, state, itemname):
        room = self.room_repository.get_by_id(state.room_id)
        player = state.player
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                print("You drop the",item.get_name())
                player.add_encumbrance(-(item.get_weight()))
                room.add_item(item.get_id())
                player.inventory.remove(item.get_id())
                return
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname in item.get_keywords():
                print("You drop the", item.get_name())
                player.add_encumbrance(-(item.get_weight()))
                room.add_item(item.get_id)
                player.inventory.remove(item.get_id())
                return
