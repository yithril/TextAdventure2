
class SkillsAction:

    def do(self, state):
        player = state.player
        print("Appraise:[{0}](INT)  Climb:[{1}](STR)  Craft Potion: [{2}](INT)  Craft Weapon: [{3}](INT)".format(player.get_skill("Appraise")+player.get_stat_modifier('intelligence'),player.get_skill("Climb")+player.get_stat_modifier('strength'),player.get_skill("Craft Potion")+player.get_stat_modifier('intelligence'),player.get_skill("Craft Weapon")+player.get_stat_modifier('intelligence')))
        print("Craft Armor:[{0}](INT)  Decipher Script: [{1}](INT)  Diplomacy:[{2}](CHA)  Heal:[{3}](WIS)".format(player.get_skill("Craft Weapon")+player.get_stat_modifier('intelligence'),player.get_skill("Decipher Script")+player.get_stat_modifier('intelligence'),player.get_skill("Diplomacy")+player.get_stat_modifier('charisma'),player.get_skill("Heal")+player.get_stat_modifier('wisdom')))
        print("Jump: [{0}](STR)  Open Lock: [{1}](DEX) Move Silently: [{2}](DEX) Swim:[{3}](STR)".format(player.get_skill("Jump")+player.get_stat_modifier('strength'),player.get_skill("Open Lock")+player.get_stat_modifier('dexterity'),player.get_skill("Move Silently")+player.get_stat_modifier('dexterity'),player.get_skill("Swim")+player.get_stat_modifier('strength')))
        print("Perception: [{0}](WIS)  Use Magic Device:[{1}](INT) Craft Spell:[{2}](INT)".format(player.get_skill("Perception")+player.get_stat_modifier('wisdom'), player.get_skill("Use Magic Device")+player.get_stat_modifier('intelligence'),player.get_skill("Craft Spell")+player.get_stat_modifier('intelligence')))

