"""The Wield action is defined as putting a weapon in main or off hand.  Non weapons cannot be wielded."""

class WieldAction():
    def __init__(self,item_repository):
        self.item_repository = item_repository

    def do(self,state,itemname):
        player = state.player
        if not itemname:
            print("Wield what?")
            return
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                #Is it a weapon
                if item.get_type() != "Weapon":
                    print("That cannot be wielded.")
                    return
                #Does your class allow you to wield this?
                elif item.get_weapon_type() not in player.guild.get_allowed_weapon_types():
                    print("{0}s are not allowed to wield {1}s".format(player.guild.get_name(), item.get_weapon_type()))
                    return
                #Druids can't wield metal objects
                elif player.guild.get_name() == "Druid" and item.get_material() in ["iron", "steel", "copper", "bronze"]:
                    print("Druids may not wield weapons made of metal.")
                    return
                elif item.get_handed() == 2:
                    if player.race.get_body_slot("Main Hand")==0 and player.race.get_body_slot("Off Hand") == 0:
                        player.race.set_body_slot("Main Hand", item.get_id())
                        player.race.set_body_slot("Off Hand", item.get_id())
                        print("You wield the {0} in both hands.".format(item.get_name()))
                        player.inventory.remove(item.get_id())
                        return
                    else:
                        print("You need two free hands to wield the {0}.".format(item.get_name()))
                        return
                elif player.race.get_body_slot("Main Hand") != 0:
                    if "Two Weapon Fighting" not in player.get_feats():
                        print("You cannot dual wield.")
                        return
                    elif player.race.get_body_slot("Off Hand") != 0:
                        offhanditem = self.item_repository.get_by_id(player.race.get_body_slot("Off Hand"))
                        print("You are already wielding {0} in your off hand.".format(offhanditem.get_name()))
                        return
                    else:
                        player.race.set_body_slot("Off Hand", item.get_id())
                        print("You wield the {0} in your off hand.".format(item.get_name()))
                        player.inventory.remove(item.get_id())
                else:
                    player.race.set_body_slot("Main Hand", item.get_id())
                    print("You wield the {0} in your main hand.".format(item.get_name()))
                    player.inventory.remove(item.get_id())
            if itemname in item.get_keywords():
                #Is it a weapon
                if item.get_type() != "Weapon":
                    print("That cannot be wielded.")
                    return
                #Does your class allow you to wield this?
                elif item.get_weapon_type() not in player.guild.get_allowed_weapon_types():
                    print("{0}s are not allowed to wield {1}s".format(player.guild.get_name(), item.get_weapon_type()))
                    return
                #Druids can't wield metal objects
                elif player.guild.get_name() == "Druid" and item.get_material() in ["iron", "steel", "copper", "bronze"]:
                    print("Druids may not wield weapons made of metal.")
                    return
                elif item.get_handed() == 2:
                    if player.race.get_body_slot("Main Hand")==0 and player.race.get_body_slot("Off Hand") == 0:
                        player.race.set_body_slot("Main Hand", item.get_id())
                        player.race.set_body_slot("Off Hand", item.get_id())
                        print("You wield the {0} in both hands.".format(item.get_name()))
                        player.inventory.remove(item.get_id())
                        return
                    else:
                        print("You need two free hands to wield the {0}.".format(item.get_name()))
                        return
                elif player.race.get_body_slot("Main Hand") != 0:
                    if "Two Weapon Fighting" not in player.get_feats():
                        print("You cannot dual wield.")
                        return
                    elif player.race.get_body_slot("Off Hand") != 0:
                        offhanditem = self.item_repository.get_by_id(player.race.get_body_slot("Off Hand"))
                        print("You are already wielding {0} in your off hand.".format(offhanditem.get_name()))
                        return
                    else:
                        player.race.set_body_slot("Off Hand", item.get_id())
                        print("You wield the {0} in your off hand.".format(item.get_name()))
                        player.inventory.remove(item.get_id())
                else:
                    player.race.set_body_slot("Main Hand", item.get_id())
                    print("You wield the {0} in your main hand.".format(item.get_name()))
                    player.inventory.remove(item.get_id())