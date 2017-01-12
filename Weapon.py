from items import Items


class Weapon(Items):
    def __init__(self,
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
                 handed,
                 offhand,
                 weapon_type,
                 const_damage,
                 damage_hit_dice,
                 damage_hit_dice_coefficient,
                 damage_stat,
                 damage_type):
        Items.__init__(self, name, desc, long_desc, weight, value, can_pick_up, is_magical, is_cursed, keywords,type)
        self.handed = handed
        self.offhand = offhand
        self.weapon_type = weapon_type
        self.const_damage = const_damage
        self.damage_stat = damage_stat
        self.damage_type = damage_type
        self.damage_hit_dice = damage_hit_dice
        self.damage_hit_dice_coefficient = damage_hit_dice_coefficient

    def wield(self):
        pass

    def unwield(self):
        pass

    def weapon_damage(self):
        pass
