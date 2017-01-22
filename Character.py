import math



class Character(object):
    def __init__(self, type, name, inventory, description, keywords, race, sex, guild, ac, mp, hp, strength, dexterity, constitution, intelligence, wisdom, charisma, level, gold, xp, encumbrance, feats, skills):

        self.type = type
        self._name = name
        self.inventory = inventory
        self._description = description
        self._keywords = keywords
        self._hp = int(hp)
        self._xp = int(xp)
        self._encumbrance = encumbrance
        self.race = race
        self._sex = sex
        self.guild = guild
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
        self.skills = skills

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

    def get_guild(self):
        return self.guild

    def set_hp(self,hp):
        self._hp = hp

    def set_mp(self,mp):
        self._mp = mp

    def set_race(self, race):
        self.race = race

    def set_guild(self, guild):
        self.guild = guild

    def set_name(self,name):
        self.name = name

    def set_gender(self,gender):
        self._sex = gender

    def get_gender(self):
        return self._sex

    def get_race(self):
        return self.race

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

    def add_player_level(self, number):
        self._level = self._level +number
        return self._level

    def get_gold(self):
        return self._gold

    def add_gold(self, number):
        self._gold = self._gold + number
        return self._gold

    def get_BAB(self):
        return math.floor(self.get_player_level()*self.guild.get_bab_modifier())

    def get_encumbrance(self):
        return self._encumbrance

    def get_all_skills(self):
        return self.skills

    def get_skill(self, skill):
        return self.skills.get(skill)

    def add_to_skill(self,skill, number):
        self.skills[skill] += number

    def get_all_stats(self):
        return self.stats

    """Sets target stat to a specific number"""
    def set_stat(self,stat,number):
        self.stats[stat] = number

    #Add a number to a stat
    def add_stat(self,stat,number):
        self.stats[stat] += number

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
            return math.floor((1.1487 ** (self.get_stat('strength')-10) *100))

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

    def get_ac(self, state, item_repository):
        player = state.player
        if state.player.guild.get_name() == "Monk":
            return self._ac + self.get_stat_modifier('dexterity')+self.get_stat_modifier('wisdom')+math.floor(self.get_level()/5)
        else:
            if state.player.race.get_body_slot("Body") == 0:
                return self._ac + self.get_stat_modifier('dexterity')
            else:
                item = item_repository.get_by_id(state.player.race.get_body_slot("Body"))
                maxdex = item.get_max_dex_bonus()
                if maxdex < self.get_stat_modifier('dexterity'):
                    finaldexmod = self.get_stat_modifier('dexterity') - (self.get_stat_modifier('dexterity')-maxdex)
                    return self._ac + finaldexmod
                else:
                    return self._ac + self.get_stat_modifier('dexterity')

    def get_feats(self):
        return self._feats

    def get_hp(self):
        return self._hp

    def get_mp(self):
        return self._mp

    def get_level(self):
        return self._level

    def get_xp(self):
        return self._xp

    def get_next_level(self):
        return self._level+1 * (self._level) * 500

    def get_max_hp(self):
        if (self.guild.get_hit_dice()*self.get_player_level())+(self.get_stat_modifier("constitution")*self.get_player_level()) < 0:
            return 1
        else:
            return (self.guild.get_hit_dice()*self.get_player_level())+(self.get_stat_modifier("constitution")*self.get_player_level())

    def get_max_mp(self):
        if ((self.get_stat_modifier(self.guild.get_main_stat())*self.get_player_level())  + (self.get_player_level() * self.guild.get_mana_modifier())) < 0:
            return 0
        else:
            return ((self.get_stat_modifier(self.guild.get_main_stat())*self.get_player_level())  + (self.get_player_level() * self.guild.get_mana_modifier()))



