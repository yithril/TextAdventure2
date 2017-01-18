class TakeItemAction:
    def __init__(self, room_repository, item_repository):
        self.room_repository = room_repository
        self.item_repository = item_repository

    def do(self, state, itemname):
        room = self.room_repository.get_by_id(state.room_id)
        player = state.player
        for itemid in room.get_item_ids():
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                print("You take the",item.get_name())
                player.inventory.append(item.get_id())
                room.remove_item(item.get_id())
                return
        for itemid in room.get_item_ids():
            item = self.item_repository.get_by_id(itemid)
            if itemname in item.get_keywords():
                print("You take the", item.get_name())
                player.inventory.append(item.get_id())
                room.remove_item(item.get_id())
                return
        return