
class Inventory:
    def __init__(self,item_repository):
        self.item_repository = item_repository

    def do(self, state):
        if not state.player.get_inventory_ids():
            return print("Your inventory is empty.")
        else:
            items = [self.item_repository.get_by_id(item) for item in state.player.get_inventory_ids()]
            item_names = [item.get_name() for item in items]
            item_names_with_articles = [
                "an {0}".format(item) if item[0] in ["a", "e", "i", "o", "u"] else "a {0}".format(item) for item in
                item_names]
            return print(Inventory.format_line(item_names_with_articles))


    @staticmethod
    def format_line(names, prefix="You have "):
        if len(names) == 1:
            return prefix+"{0}".format(names[0])
        else:
            return prefix + ", ".join(names[:-1]) + ", and " + names[-1]
