class RemoveAction:
    def __init__(self, item_repository):
        self.item_repository = item_repository

    def do(self,state, itemname):
        player = state.player
        for itemid, value in player.race.get_body_type().items():
            if value != 0:
                item = self.item_repository.get_by_id(value)
                if item.get_type() != "Armor":
                    print("The remove command can only be used with armor.")
                    return
                elif itemname == item.get_name():
                    print("You remove the {0}.".format(item.get_name()))
                    item.remove(state)
                    player.race.set_body_slot(item.get_armor_slot(), 0)
                    player.inventory.append(item.get_id())
                elif itemname in item.get_keywords():
                    print("You remove the {0}.".format(item.get_name()))
                    item.remove(state)
                    player.race.set_body_slot(item.get_armor_slot(), 0)
                    player.inventory.append(item.get_id())
                else:
                    print("You're not wearing a {0}.".format(item.get_name()))




