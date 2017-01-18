import textwrap



class Room(object):
    def __init__(self, id, name, items_inv, npc_inv, neighbors, description, terrain, indoors, lighting, room_description):
        self._id = id
        self._name = name
        self._items_inv = items_inv
        self._npc_inv = npc_inv
        self.neighbors = neighbors
        self._description = description
        self.terrain = terrain
        self.indoors = indoors
        self.lighting = lighting
        self.room_description = room_description

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

    def get_npc_inv(self):
        return self._npc_inv

    def add_npc(self, npc):
        self._npc_inv.append(npc)

    def remove_npc(self, npc):
        self._npc_inv.remove(npc)

    def get_item_ids(self):
        return self._items_inv

    def remove_item(self, item):
        self._items_inv.remove(item)

    def add_item(self, item):
        self._items_inv.append(item)

    def neighbor(self,direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

