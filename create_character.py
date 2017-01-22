import math
import textwrap
import dice_roller
import guild_loader
import race_loader
from Character import Character

def is_valid_player_name(name):
    """
    :param name: Player name to be validated
    :return: True if the name is usable to create a Player Character
    """
    return isinstance(name, str) and name is not None and name != ""

def is_valid_sex_single_character(sex):
    return sex in ['M', 'F', 'm', 'f']


def is_valid_sex_word(sex):
    sexes = ['male', 'female']
    title_case = [sex.title() for sex in sexes]
    lower_case = [sex.lower() for sex in sexes]
    upper_case = [sex.upper() for sex in sexes]

    valid_sexes = title_case + lower_case + upper_case
    return sex in valid_sexes


def is_valid_sex(sex):
    """

    :param sex: Gender of the Player to be validated
    :return: True if sex is M or F, otherwise False
    """

    return is_valid_sex_single_character(sex) or is_valid_sex_word(sex)

class create_Character:

    def generate(self):
        the_player = Character(name="", type = "Character", keywords = [], race = None, guild = None, sex = "", description = "", inventory = [], ac = 10, hp = 0, mp = 0, encumbrance = 0, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0, level =1, gold = 0, xp = 0, feats = 0, skills = {"Appraise": 0,
            "Climb" : 0,
            "Craft Potion" : 0,
            "Craft Spell" : 0,
            "Craft Weapon": 0,
            "Craft Armor" : 0,
            "Decipher Script": 0,
            "Diplomacy": 0,
            "Heal": 0,
            "Jump": 0,
            "Open Lock": 0,
            "Move Silently":0,
            "Swim":0,
            "Perception":0,
            "Use Magic Device": 0})
        name = ""
        races = race_loader.load_races()
        race_map = dict( (race.get_name(), race) for race in races)
        guilds = guild_loader.load_guilds()
        guild_map = dict((guild.get_name(), guild) for guild in guilds)
        race_name = None
        while name == "":
            name = input("What name do you want your character to have?: ")
            if is_valid_player_name(name):
                print("Your character name is ",name)
                the_player.set_name(name)
            else:
                print("Sorry, %s is not a valid name." % (name))
                continue
        while True:
            sex = input("Is your character Male or Female? (M/F)")
            if is_valid_sex(sex):
                print("Gender chosen.")
                if (sex.lower() == "m" or sex.lower() == "male"):
                    the_player.set_gender("Male")
                else:
                    the_player.set_gender("Female")
                break
            else:
                print("Sorry, that is not a valid gender.  Valid gender is M/F")
                continue
        while race_name not in race_map:
            race_name = input("Select a race from [%s] or for information type info {race}: " % ", ".join(sorted(race_map.keys())))
            if race_name.startswith("info "):
                info_name = race_name[4:].strip()
                if info_name in race_map:
                    race = race_map[info_name]
                    for line in textwrap.wrap(race.get_desc(), 72):
                        print(line)
                else:
                    print("Unknown race:", info_name)
        """Player race is now set"""
        player_race = race_map[race_name]
        the_player.set_race(player_race)
        print("Selected race was:", player_race)
        guild_name = None
        while guild_name not in guild_map:
            guild_name = input("Select a class from [%s] or for more information type info [class]: " % ", ".join(sorted(guild_map.keys())))
            if guild_name.startswith("info "):
                info_name = guild_name[4:].strip()
                if info_name in guild_map:
                    guild = guild_map[info_name]
                    for line in textwrap.wrap(guild.get_desc(), 72):
                        print(line)
                else:
                    print("Unknown class: ", info_name)
        """Player Class is now set"""
        player_class = guild_map[guild_name]
        the_player.set_guild(player_class)
        print("Selected class was:", guild_name)
        print("The computer will roll dice and give you six numbers.")
        print("You must assign one of the six numbers to one of your six stats.")
        print("Remember, certain classes prioritize certain stats over others.")
        die_rolls = dice_roller.roll_stats()
        print("You have the following die rolls:")
        print(die_rolls)
        while True:
            temp = input("You are allowed to re-roll your stats ONCE.  Previous rolls cannot be regained.  Would you like to re-roll? Y/N")
            if (temp.lower() == "y" or temp.lower() == "yes"):
                die_rolls = dice_roller.roll_stats()
                print("Your new rolls.")
                print(die_rolls)
                break
            else:
                print("Die rolls accepted.")
                break
        while True:
            print("Racial stat modifiers will be applied AFTER you select a value for your stat.")
            try:
                strength = int(input("Which roll do you want to assign to Strength?"))
                if strength in die_rolls:
                    print("Strength is set to : ", strength)
                    die_rolls.remove(strength)
                    strength += player_race.get_single_attribute('STR')
                    the_player.set_stat('strength',strength)
                    break
                else:
                    print("That is not one of your die rolls.")
                    print("You can select from the following scores: ", die_rolls)
                    continue
            except ValueError:
                print("Needs to be a number")
        while True:
            try:
                dexterity = int(input("Which roll do you want to assign to Dexterity?"))
                if dexterity in die_rolls:
                    print("Dexterity is set to : ", dexterity)
                    die_rolls.remove(dexterity)
                    dexterity+= player_race.get_single_attribute('DEX')
                    the_player.set_stat('dexterity', dexterity)
                    break
                else:
                    print("That is not one of your die rolls.")
                    print("You can select from the following scores: ", die_rolls)
                    continue
            except ValueError:
                print("Needs to be a number")
        while True:
            try:
                constitution = int(input("Which roll do you want to assign to Constitution?"))
                if constitution in die_rolls:
                    print("Constitution is set to : ", constitution)
                    die_rolls.remove(constitution)
                    constitution += player_race.get_single_attribute('CON')
                    the_player.set_stat('constitution', constitution)
                    break
                else:
                    print("That is not one of your die rolls.")
                    print("You can select from the following scores: ", die_rolls)
                    continue
            except ValueError:
                print("Needs to be a number")
        while True:
            try:
                intelligence = int(input("Which roll do you want to assign to Intelligence?"))
                if intelligence in die_rolls:
                    print("Intelligence is set to : ", intelligence)
                    die_rolls.remove(intelligence)
                    intelligence += player_race.get_single_attribute('INT')
                    the_player.set_stat('intelligence', intelligence)
                    break
                else:
                    print("That is not one of your die rolls.")
                    print("You can select from the following scores: ", die_rolls)
                    continue
            except ValueError:
                print("Needs to be a number")
        while True:
            try:
                wisdom = int(input("Which roll do you want to assign to Wisdom?"))
                if wisdom in die_rolls:
                    print("Wisdom is set to : ", wisdom)
                    die_rolls.remove(wisdom)
                    wisdom += player_race.get_single_attribute('WIS')
                    the_player.set_stat('wisdom', wisdom)
                    break
                else:
                    print("That is not one of your die rolls.")
                    print("You can select from the following scores: ", die_rolls)
                    continue
            except ValueError:
                print("Needs to be a number")
        while True:
            try:
                charisma = int(input("Which roll do you want to assign to Charisma?"))
                if charisma in die_rolls:
                    print("Charisma is set to : ", charisma)
                    die_rolls.remove(charisma)
                    charisma += player_race.get_single_attribute('CHA')
                    the_player.set_stat('charisma', charisma)
                    break
                else:
                    print("That is not one of your die rolls.")
                    print("You can select from the following scores: ", die_rolls)
                    continue
            except ValueError:
                print("Needs to be a number")
        print("Stat appropriation complete.")
        print("Now selecting skills...")
        print("It costs 1 point to raise a class skill.  Non-class skills are 2 points.")
        skill_points = player_class.get_skill_points()+math.floor(((intelligence/2)-5))
        if the_player.race.get_name() == "Human":
            skill_points +=4
        while skill_points > 0:
            print("Which skill would you like to increase?")
            print("You have {0} skill points remaining.".format(skill_points))
            skill_map=[value for value in player_class.get_class_skill_cost() if player_class.get_class_skill_cost()[value] == 1]
            print("Your class skills:",skill_map)
            print("Appraise:[{0}]  Climb:[{1}]  Craft Potion: [{2}]  Craft Weapon: [{3}]".format(the_player.get_skill("Appraise"), the_player.get_skill("Climb"), the_player.get_skill("Craft Potion"),the_player.get_skill("Craft Weapon")))
            print("Craft Armor: [{0}]  Decipher Script: [{1}]  Diplomacy:[{2}]  Heal:[{3}]".format(the_player.get_skill("Craft Weapon"), the_player.get_skill("Decipher Script"), the_player.get_skill("Diplomacy"),the_player.get_skill("Heal")))
            print("Jump: [{0}] Open Lock: [{1}] Move Silently: [{2}] Swim: [{3}]".format(the_player.get_skill("Jump"),the_player.get_skill("Open Lock"),the_player.get_skill("Move Silently"),the_player.get_skill("Swim")))
            print("Perception: [{0}]  Use Magic Device: [{1}] Craft Spell:[{2}]".format(the_player.get_skill("Perception"),the_player.get_skill("Use Magic Device"),the_player.get_skill("Craft Spell")))
            skill_choice = input("Which skill would you like to raise?").title()
            if skill_choice not in the_player.get_all_skills():
                print("You cannot select that skill.")
                continue
            else:
                question = input("That will cost {0} point(s) to raise one rank.  Are you sure? Y/N".format(player_class.get_class_skill(skill_choice)))
                if question == "No" or question == "no" or question == "n" or question == "N":
                    print("Understood.")
                    continue
                else:
                    if player_class.get_class_skill(skill_choice) > skill_points:
                        print("You do not have enough skill points to do that.")
                        continue
                    elif player_class.get_class_skill(skill_choice) == 1:
                        if the_player.get_skill(skill_choice)+1 > 4:
                            print("Sorry, that max rank for a class skill is 4.")
                        else:
                            print("{0} was raised one rank.".format(skill_choice))
                            the_player.add_to_skill(skill_choice, 1)
                            skill_points -= player_class.get_class_skill(skill_choice)
                            continue
                    elif player_class.get_class_skill(skill_choice) == 2:
                        if the_player.get_skill(skill_choice)+1 > 2:
                            print("Sorry, that max rank for a non class skill is 2.")
                            continue
                        else:
                            print("{0} was raised one rank.".format(skill_choice))
                            the_player.add_to_skill(skill_choice, 1)
                            skill_points -= player_class.get_class_skill(skill_choice)
                            continue

        print("Skill points allocated.")
        the_player.set_hp(player_class.get_hit_dice() + the_player.get_stat_modifier('constitution'))
        if player_class.get_mana_modifier() == 0:
            the_player.set_mp(0)
        else:
            the_player.set_mp(player_class.get_mana_modifier() * the_player.get_level() + the_player.get_stat_modifier(player_class.get_main_stat()))
        print('You are {0}, a level {1} {2} {3} {4} with {5} hit points and {6} mana points'.format(the_player.get_name(), the_player.get_level(), the_player.get_gender(), player_race.get_name(), player_class.get_name(), the_player.get_hp(), the_player.get_mp()))
        print('Your stats are Strength: {0}, Constitution: {1}, Dexterity: {2}, Intelligence: {3}, Charisma: {4}, Wisdom: {5}'.format(the_player.get_stat('strength'),the_player.get_stat('constitution'),the_player.get_stat('dexterity'),the_player.get_stat('intelligence'),the_player.get_stat('charisma'),the_player.get_stat('wisdom')))
        return the_player