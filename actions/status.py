
class StatusAction:
    def __init__(self, item_repository):
        self.item_repository = item_repository

    def do(self, state):
        player = state.player
        print("Current HP: {0}/{1} Current MP: {2}/{3}  Level: {4} XP: {5}/{6} AC: {7} Encumbrance: {8}/{9}".format(player.get_hp(), player.get_max_hp(), player.get_mp(), player.get_max_mp(), player.get_level(), player.get_xp(), player.get_next_level(), player.get_ac(state, self.item_repository),player.get_encumbrance(), player.get_max_encumbrance()))


