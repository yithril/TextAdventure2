import math


class Character(object):
    def __init__(self, type, name, inventory, description, keywords, race, sex, guild, ac, mp, hp, strength, dexterity, constitution, intelligence, wisdom, charisma, level, gold, xp, encumbrance, feats):

        self.type = type
        self._name = name
        self.inventory = inventory
        self._description = description
        self._keywords = keywords
        self._hp = int(hp)
        self._xp = int(xp)
        self._encumbrance = encumbrance
        self._race = race
        self._sex = sex
        self._guild = guild
        self._level = int(level)
        self._mp = int(mp)
        self._ac = int(ac)
        self._gold = int(gold)
        self._feats = feats
        self.stats = {
            "strength": int(strength),
            "dexterity": int(dexterity),
            "constitution": int(constitution),
            "wisdom": int(intelligence),
            "intelligence": int(wisdom),
            "charisma": int(charisma)
        }

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __repr__(self):
        return "[name: \"%s\"]" % self.get_name()

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self._name

    def get_inventory_ids(self):
        return self.inventory

    def get_description(self):
        return self._description

    def get_keywords(self):
        return self._keywords

    def get_player_level(self):
        return self._level

    def get_gold(self):
        return self._gold

    def get_encumbrance(self):
        return self._encumbrance

    """Sets target stat to a specific number"""
    def set_stat(self,stat,number):
        self.stats[stat] = number

    """This function gets a specific stat"""

    def get_stat(self, stat):
        return self.stats[stat]

    """This function gets a specific stat's modifier"""

    def get_stat_modifier(self, stat):
        modifier = math.floor((self.get_stat(stat) / 2) - 5)
        return modifier

    """maximum player can carry"""
    def get_max_encumbrance(self):
        if self.get_stat('strength') < 10:
            return self.get_stat('strength')*10
        else:
            return math.floor((1.1487 ** (self.get_stat('strength')) *100))

    """tests if encumbrance is higher than max"""
    def is_too_heavy(self, weight):
        if self.get_max_encumbrance() < self._encumbrance + weight:
            return True
        else:
            return False

    def add_encumbrance(self, weight):
        self._encumbrance = self._encumbrance + weight
        return self._encumbrance

    def add_ac(self, number):
        self._ac = self._ac + number
        return self._ac

    def get_ac(self):
        return self._ac