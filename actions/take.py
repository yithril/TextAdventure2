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
                if item.get_can_pick_up() == "False":
                    print("That is not something you can take.")
                    return
                if player.is_too_heavy(item.get_weight()) == True:
                    print("Taking that would make you over encumbeed.")
                    return
                print("You take the",item.get_name())
                player.inventory.append(item.get_id())
                player.add_encumbrance(item.get_weight())
                room.remove_item(item.get_id())
                return
        for itemid in room.get_item_ids():
            item = self.item_repository.get_by_id(itemid)
            if itemname in item.get_keywords():
                if item.get_can_pick_up() == "False":
                    print("That is not something you can take.")
                    return
                if player.is_too_heavy(item.get_weight()) == True:
                    print("Taking that would make you over encumbeed.")
                    return
                print("You take the", item.get_name())
                player.inventory.append(item.get_id())
                player.add_encumbrance(item.get_weight())
                room.remove_item(item.get_id())
                return
        return


    @staticmethod
    def check_can_pick_up(item):
        if item.get_can_pick_up() == "False":
            print("That is not something you can take.")


    @staticmethod
    def item_too_heavy(state, item):
        if state.player.is_too_heavy(item.get_weight()) == False:
            print("Taking that item would make you over encumbered.")
            return False
        else:
            return True
