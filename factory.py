
from Armor import Armor
from Character import Character
from Weapon import Weapon
from Wands import Wands
from room import Room

class Chained_Factory():
    def __init__(self, factories):
        self._factories = factories

    def create(self, d):
        for f in self._factories:
            l = f.create(d)
            if l:
                return l

def Generic_Factory(clazz):
    class Anon:
        def create(self, d):
            return clazz(**d)
    return Anon


def make_typed_factory(clazz):
    Generic_Factory_Class = Generic_Factory(clazz)
    fact = Generic_Factory_Class()
    class Anon:
        def create(self, d):
            if clazz.__name__ == d.get("type"):
                return fact.create(d)
    return Anon

Room_Factory_Class = Generic_Factory(Room)
Weapon_Factory_Class = make_typed_factory(Weapon)
Armor_Factory_Class = make_typed_factory(Armor)
Wand_Factory_Class = make_typed_factory(Wands)
Character_Factory_Class = Generic_Factory(Character)


Room_Factory = Room_Factory_Class()
Weapon_Factory = Weapon_Factory_Class()
Armor_Factory = Armor_Factory_Class()
Wand_Factory = Wand_Factory_Class()
Character_Factory = Character_Factory_Class()

Item_Factory = Chained_Factory([Weapon_Factory,Armor_Factory,Wand_Factory])


