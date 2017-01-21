
class UnwieldAction:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def do(self,state, itemname):
        player = state.player
        for itemid, value in player.race.get_body_type().items():
            if value != 0:
                item = self.item_repository.get_by_id(value)
                if item.get_type() != "Weapon":
                    print("The unwield command can only be used with weapons.")
                    return
                elif itemname == item.get_name():
                    if item.get_id() == player.race.get_body_slot("Main Hand"):
                        print("You unwield the {0}.".format(item.get_name()))
                        player.race.set_body_slot("Main Hand", 0)
                        player.inventory.append(item.get_id())
                    elif item.get_id() == player.race.get_body_slot("Off Hand"):
                        print("You unwield the {0}.".format(item.get_name()))
                        player.race.set_body_slot("Off Hand", 0)
                        player.inventory.append(item.get_id())
                    else:
                        print("You're not wielding a {0}.".format(item.get_name()))
                elif itemname in item.get_keywords():
                    if item.get_id() == player.race.get_body_slot("Main Hand"):
                        print("You unwield the {0}.".format(item.get_name()))
                        player.race.set_body_slot("Main Hand", 0)
                        player.inventory.append(item.get_id())
                    elif item.get_id() == player.race.get_body_slot("Off Hand"):
                        print("You unwield the {0}.".format(item.get_name()))
                        player.race.set_body_slot("Off Hand", 0)
                        player.inventory.append(item.get_id())
                    else:
                        print("You're not wielding a {0}.".format(item.get_name()))


