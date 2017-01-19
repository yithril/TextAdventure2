import json
import textwrap





def is_none_or_white_space(text):
    return text is None or text.isspace() or text == ""



class Room():
    def __init__(self,
                 id,
                 name,
                 description,
                 neighbors,
                 npc_inv,
                 items_inv,
                 indoors,
                 terrain,
                 ):
        self._indoors = indoors
        self._items_inv = items_inv
        self._npc_inv = npc_inv
        self._id = id
        self._name = name
        self._description = description
        self.neighbors = neighbors
        self._terrain = terrain

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

    def neighbor(self,direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self.neighbor('n')
    def south(self):
        return self.neighbor('s')
    def east(self):
        return self.neighbor('e')
    def west(self):
        return self.neighbor('w')

    def print_room(self, room):
        print(room._name)
        print("")
        for line in textwrap.wrap(room._description,72):
            print(line)
        print("Exits: ",room._neighbors)
        if self._npc_inv:
            self.get_room_npc_description(self._npc_inv)
        if self._items_inv:
            self.get_item_descriptions(self._items_inv)
    
    def get_room_npc_description(self, npcs):
        name_map = [npcs.character.get_name() for npc in npcs]
        if len(npcs) == 1:
            return print("You see {0} here.".format(name_map))
        elif len(npcs) == 2:
            return print("You see {0} and {1} here.".format(name_map[0], name_map[1]))
        else:
            name_map = [npcs.character.get_name() for npc in npcs[:-1]]
            name_map = ", ".join(name_map)
            last_npc = npcs[-1].character.get_name()
            return print("You see " + name_map,"and " +last_npc)
    
    def get_item_descriptions(self, items):
        item_map = [items.Items.get_name() for item in items]
        item_map = ["an {0}".format(item) if item[0] in ["a","e","i","o","u"] else "a {0}".format(item) for item in item_map]
        last_item = item_map[-1]
        if len(item_map) == 1:
            return print("You see {0} here.".format(item_map))
        elif len(item_map) == 2:
            return print("You see {0} and {1} here.".format(item_map[0], item_map[1]))
        else:
            return print("You see {0} and {1}".format(item_map,last_item))

    def get_items_inv(self):
        return self._items_inv

    """NPC related functions"""
    def add_npc(self, npc):
        self._npc_inv.append(npc)

    def remove_npc(self, npc):
        self._npc_inv.remove(npc)

    def get_empty(self):
        if len(self._npc_inv) == 0:
            return True
        else:
            return False

    def get_id(self):
        return self._id
    



    """Item related functions"""
    def add_item_to_room(self, item):
        self._items_inv.append(item)

    def remove_item_from_room(self, item):
        self._items_inv.remove(item)

    def get_empty_of_items(self):
        if len(self._items_inv) == 0:
            return True
        else:
            return False

    """    def get_room_item_description(self, items):
        name_map = ["an ".join(items.items.get_name()) if items[0] in ["a","e","i","o","u","h"] else "a ".join(items.items.get_name()) for items in items]
        if len(items) == 1:
            return print("You see {0} here.".format(name_map[0]))
        elif len(items) == 2:
            return print("You see {0} and {1} here.".format(name_map[0], name_map[1]))
        else:
            last_npc = name_map[-1]
            name_map = ", ".join(name_map)
            return print("You see " + name_map,"and " +last_npc)"""





