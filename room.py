
class Room(object):
    def __init__(self, id, name, items_inv, npc_inv, neighbors, description, terrain, indoors):
        self._id = id
        self._name = name
        self._items_inv = items_inv
        self._npc_inv = npc_inv
        self.neighbors = neighbors
        self._description = description
        self.terrain = terrain
        self.indoors = indoors

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

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def get_name(self):
        return self._name

    def neighbor(self,direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def get_room_npc_description(self):
        npcs = self._npc_inv
        name_map = [npcs.character.get_name() for npc in npcs]
        if len(npcs) == 1:
            return "You see {0} here.".format(name_map)
        elif len(npcs) == 2:
            return "You see {0} and {1} here.".format(name_map[0], name_map[1])
        else:
            name_map = [npcs.character.get_name() for npc in npcs[:-1]]
            name_map = ", ".join(name_map)
            last_npc = npcs[-1].character.get_name()
            return "You see " + name_map, "and " + last_npc

    def get_item_descriptions(self):
        items = self._items_inv
        item_map = [items.Items.get_name() for item in items]
        item_map = ["an {0}".format(item) if item[0] in ["a", "e", "i", "o", "u"] else "a {0}".format(item) for item in
                    item_map]
        last_item = item_map[-1]
        if len(item_map) == 1:
            return "You see {0} here.".format(item_map)
        elif len(item_map) == 2:
            return "You see {0} and {1} here.".format(item_map[0], item_map[1])
        else:
            return "You see {0} and {1}".format(item_map, last_item)