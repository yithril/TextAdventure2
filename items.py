import random


class Items(object):
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
                 ):

        self._weight = int(weight)
        self._name = name
        self._desc = desc
        self._long_desc = long_desc
        self._value = int(value)
        self._can_pick_up = can_pick_up
        self._is_magical = is_magical
        self._is_cursed = is_cursed
        self._keywords = keywords
        self.type = type


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

    def get_short_desc(self):
        return self._desc

    def get_long_desc(self):
        return self._long_desc

    def get_value(self):
        return self._value

    def get_can_pick_up(self):
        return self._can_pick_up

    def get_weight(self):
        return self._weight
