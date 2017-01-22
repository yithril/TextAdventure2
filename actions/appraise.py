
class AppraiseAction:
    def __init__(self,item_repository):
        self.item_repository = item_repository

    def do(self, state, itemname):
        player = state.player
        for itemid in player.inventory:
            item = self.item_repository.get_by_id(itemid)
            if itemname == item.get_name():
                print("You carefully examine the {0}.".format(item.get_name()))
                if player.get_skill('Appraise')+10+player.get_stat_modifier('intelligence') >= item.get_item_appraise_dc():
                    print(item.get_short_desc())
                    print("You estimate it is worth {0} gold pieces.".format(item.get_value()))
                    return
                else:
                    print("You cannot ascertain what the item does or how much it is worth.")
            elif itemname in item.get_keywords():
                print("You carefully examine the {0}.".format(item.get_name()))
                if player.get_skill('Appraise') + 10+player.get_stat_modifier('intelligence') >= item.get_item_appraise_dc():
                    print(item.get_short_desc())
                    print("You estimate it is worth {0} gold pieces.".format(item.get_value()))
                    return
                else:
                    print("You cannot ascertain what the item does or how much it is worth.")
