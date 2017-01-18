

class Character(object):
    def __init__(self, name, inventory, type):
        assert isinstance(inventory, list)
        self.inventory = inventory
        self.name = name
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
        return self.name
