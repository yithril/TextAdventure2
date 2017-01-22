"""Wear action is specifically for armor and shields"""

class WearArmorAction:
    def __init__(self, item_repository):
        self.item_repository = item_repository

    def do(self, state, itemname):
        player = state.player
        if not itemname:
            print("Wear what?")
            return
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                #Only Armor can be worn
                    if item.get_type() != "Armor":
                        print("That cannot be worn.")
                        return
                    elif item.get_armor_level() > player.guild.get_equipment_type():
                        print("That armor is too cumbersome for {0}s to wear.".format(player.guild.get_name()))
                        return
                    elif item.get_armor_slot() == "Ring":
                        if player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is not 0:
                            print("Both your ring slots are full.")
                            return
                        elif player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is 0:
                            player.race.set_body_slot("Ring Slot 2", item.get_id())
                            print("You wear the {0} in your second ring slot.".format(item.get_name()))
                            item.equip(state)
                            player.inventory.remove(item.get_id())
                            return
                        else:
                            player.race.set_body_slot("Ring Slot 1", item.get_id())
                            print("You wear the {0}".format(item.get_name()))
                            item.equip(state)
                            player.inventory.remove(item.get_id())
                            return
                    elif player.race.get_body_slot(item.get_armor_slot()) != 0:
                        print("You are already wearing something in your {0} slot.".format(item.get_armor_slot().lower()))
                        return
                    else:
                        player.race.set_body_slot(item.get_armor_slot(), item.get_id())
                        print("You wear the {0}".format(item.get_name()))
                        item.equip(state)
                        player.inventory.remove(item.get_id())
                        return
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname in item.get_keywords():
                #Only Armor can be worn
                    if item.get_type() != "Armor":
                        print("That cannot be worn.")
                        return
                    elif item.get_armor_level() > player.guild.get_equipment_type():
                        print("That armor is too cumbersome for {0}s to wear.".format(player.guild.get_name()))
                        return
                    elif item.get_armor_slot() == "Ring":
                        if player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is not 0:
                            print("Both your ring slots are full.")
                            return
                        elif player.race.get_body_slot("Ring Slot 1") is not 0 and player.race.get_body_slot("Ring Slot 2") is 0:
                            player.race.set_body_slot("Ring Slot 2", item.get_id())
                            print("You wear the {0} in your second ring slot.".format(item.get_name()))
                            item.equip(state)
                            player.inventory.remove(item.get_id())
                            return
                        else:
                            player.race.set_body_slot("Ring Slot 1", item.get_id())
                            print("You wear the {0}".format(item.get_name()))
                            item.equip(state)
                            player.inventory.remove(item.get_id())
                            return
                    elif player.race.get_body_slot(item.get_armor_slot()) != 0:
                        print("You are already wearing something in your {0} slot.".format(item.get_armor_slot().lower()))
                        return
                    else:
                        player.race.set_body_slot(item.get_armor_slot(), item.get_id())
                        print("You wear the {0}".format(item.get_name()))
                        item.equip(state)
                        player.inventory.remove(item.get_id())
                        return

