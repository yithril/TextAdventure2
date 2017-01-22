from collections import OrderedDict

class StatsAction:

    def do(self, state):
        base = OrderedDict()
        base["Strength"] = state.player.get_stat('strength')
        base["Constitution"] = state.player.get_stat('constitution')
        base["Dexterity"] = state.player.get_stat('dexterity')
        base["Intelligence"] = state.player.get_stat('intelligence')
        base["Wisdom"] = state.player.get_stat('wisdom')
        base["Charisma"] = state.player.get_stat('charisma')

        print("Strength: {0}[{1}] Constitution: {2}[{3}] Dexterity: {4}[{5}] Intelligence: {6}[{7}] Wisdom: {8}[{9}] Charisma: {10}[{11}]".format(base["Strength"],state.player.get_stat_modifier('strength'),base["Constitution"],state.player.get_stat_modifier('constitution'),base["Dexterity"],state.player.get_stat_modifier('dexterity'),base["Intelligence"],state.player.get_stat_modifier('intelligence'),base["Wisdom"],state.player.get_stat_modifier('wisdom'),base["Charisma"],state.player.get_stat_modifier('charisma')))
