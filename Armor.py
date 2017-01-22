from items import Items


class Armor(Items):
    def __init__(self,
                 id,
                 name,
                 desc,
                 long_desc,
                 weight,
                 value,
                 can_pick_up,
                 is_magical,
                 is_cursed,
                 keywords,
                 type,
                 material,
                 appraise_dc,
                 slot,
                 armor_ac,
                 max_dex_bonus,
                 armor_level,
                 attribute_boost):
        super().__init__(id, name, desc, long_desc, weight, value, can_pick_up, is_magical, is_cursed, keywords, type, material, appraise_dc)
        self._slot = str(slot)
        self.armor_ac = armor_ac
        self.max_dex_bonus = max_dex_bonus
        self.armor_level = armor_level
        self.attribute_boost = attribute_boost

    def get_armor_level(self):
        return self.armor_level

    def get_armor_slot(self):
        return self._slot

    def get_max_dex_bonus(self):
        return self.max_dex_bonus

    def equip(self, state):
        player = state.player
        #Adjust AC
        player.add_ac(self.armor_ac)
        #Adjust a stat or skill
        for key in self.attribute_boost:
            if key in player.get_all_stats():
                player.add_stat(key, self.attribute_boost.get(key))
            elif key in player.get_all_skills():
                player.add_to_skill(key, self.attribute_boost.get(key))

    def remove(self, state):
        player = state.player
        player.add_ac(-(self.armor_ac))
        for key in self.attribute_boost:
            if key in player.get_all_stats():
                player.add_stat(key, -(self.attribute_boost.get(key)))
            elif key in player.get_all_skills():
                player.add_to_skill(key, -(self.attribute_boost.get(key)))

    def armor_class(self):
        pass
