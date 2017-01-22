import math


class Guild():
    def __init__(self, name,
                 desc,
                 bab_modifier,
                 fort_save,
                 will_save,
                 ref_save,
                 equipment_type,
                 hit_dice,
                 mana_modifier,
                 class_skill_cost,
                 allowed_weapon_types,
                 main_stat,
                 skill_points,):

        self._name = name
        self._desc = desc
        self._bab_modifier = bab_modifier
        self._fort_save = fort_save
        self._will_save = will_save
        self._ref_save = ref_save
        self._equipment_type = equipment_type
        self._hit_dice = hit_dice
        self._mana_modifier = mana_modifier
        self._allowed_weapon_types = allowed_weapon_types
        self.skill_points = skill_points
        self.main_stat = main_stat
        self._class_skill_cost = class_skill_cost

    def get_main_stat(self):
        return self.main_stat

    def get_name(self):
        return self._name

    def get_desc(self):
        return self._desc

    def get_skill_points(self):
        return self.skill_points

    def get_bab_modifier(self):
        return self._bab_modifier

    def get_allowed_weapon_types(self):
        return self._allowed_weapon_types

    """Checks for Light, Medium, or Heavy Armor"""
    def get_equipment_type(self):
        return self._equipment_type

    def get_hit_dice(self):
        return self._hit_dice

    def get_mana_modifier(self):
        return self._mana_modifier

    """Get the cost of different skills"""
    def get_class_skill_cost(self):
        return self._class_skill_cost.copy()

    def get_class_skill(self, skill):
        return self._class_skill_cost.get(skill)

    def get_fort_save(self):
        return self._fort_save

    def get_will_save(self):
        return self._will_save

    def get_reflex_save(self):
        return self._ref_save

    @staticmethod
    def calculate_save(save_type, level):
        return  math.floor((level/2)+2) if "Strong" == save_type else math.floor(level/3)

    def calculate_fort_save(self, level):
        return Guild.calculate_save(self.get_fort_save(), level)

    def calculate_ref_save(self, level):
        return Guild.calculate_save(self.get_reflex_save(), level)

    def calculate_will_save(self, level):
        return Guild.calculate_save(self.get_will_save(), level)