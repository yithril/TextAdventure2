from items import Items


class Armor(Items):
    def __init__(self,
                 name,
                 desc,
                 long_desc,
                 weight,
                 value,
                 can_pick_up = False,
                 is_magical = False,
                 is_cursed = False,
                 keywords =[],
                 slot = None,
                 armor_ac = 0):
        Items.__init__(self, name, desc, long_desc, weight, value, can_pick_up, is_magical, is_cursed, keywords)
        self.slot = slot,
        self.armor_ac = armor_ac

    def equip(self):
        pass

    def remove(self):
        pass

    def armor_class(self):
        pass

    def adjust_stat(self, amount):
        pass