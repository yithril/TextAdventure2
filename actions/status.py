
class StatusAction:

    def do(self, state):
        player = state.player
        print("Current HP: {0}/{1} Current MP: {2}/{3}  Level: {4} XP: {5}/{6} Encumbrance: {7}/{8}".format(player.get_hp(), player.get_max_hp(), player.get_mp(), player.get_max_mp(), player.get_level(), player.get_xp(), player.get_next_level(), player.get_encumbrance(), player.get_max_encumbrance()))


