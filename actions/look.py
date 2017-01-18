from Game_Screen import Game_Screen
import textwrap


class LookAction:
    def __init__(self, room_repository, npc_repository, item_repository):
        self.room_repository = room_repository
        self.npc_repository = npc_repository
        self.item_repository = item_repository

    def print_npc(self, npc):
        for line in textwrap.wrap(npc.get_description(),72):
            print(line)

    def print_item(self, item):
        for line in textwrap.wrap(item.get_long_desc(),72):
            print(line)

    def print_room(self, room):
        print(room.get_name())
        print("")
        for line in textwrap.wrap(room.get_description(), 72):
            print(line)
        exits = []
        for key in room.neighbors.keys():
            exits.append(key)
        print("Exits:", exits)
        if room.get_npc_inv():
            print(self.get_room_npc_description(room))
        else:
            print("No one is here.")
        if room.get_item_ids():
            print(self.get_item_descriptions(room))

    @staticmethod
    def format_line(names, prefix="You see ", suffix=" here."):
        if len(names) == 1:
            return prefix+"{0}".format(names[0])+suffix
        else:
            return prefix + ", ".join(names[:-1]) + ", and " + names[-1] + suffix

    def get_room_npc_description(self, room):
        names = [self.npc_repository.get_by_id(npc).get_name() for npc in room.get_npc_inv()]
        return LookAction.format_line(names)


    def get_item_descriptions(self, room):
        items = [self.item_repository.get_by_id(item) for item in room.get_item_ids()]
        item_names = [item.get_name() for item in items]
        item_names_with_articles = ["an {0}".format(item) if item[0] in ["a", "e", "i", "o", "u"] else "a {0}".format(item) for item in
                    item_names]
        return LookAction.format_line(item_names_with_articles)


    def do(self, state, direction):
        room = self.room_repository.get_by_id(state.room_id)
        if direction and direction != "here":
            if room.neighbor(direction):
                room = room.neighbor(direction)
            else:
                # is it an item
                for item_id in room.get_item_ids():
                    item = self.item_repository.get_by_id(item_id)
                    if item.get_name() == direction:
                        return self.print_item(item)
                for item_id in room.get_item_ids():
                    item = self.item_repository.get_by_id(item_id)
                    if direction in item.get_keywords():
                        return self.print_item(item)
                # is it an npc
                for npc_id in room.get_npc_inv():
                    npc = self.npc_repository.get_by_id(npc_id)
                    if npc.get_name() == direction:
                        return self.print_npc(npc)
                for npc_id in room.get_npc_inv():
                    npc = self.npc_repository.get_by_id(npc_id)
                    if direction in npc.get_keywords():
                        return self.print_npc(npc)

                return "Can't look that way"

        return self.print_room(room)















