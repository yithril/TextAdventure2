
from Armor import Armor
from Character import Character
from room import Room
from Weapon import Weapon
from Wands import Wands

class Chained_Factory():
    def __init__(self, factories):
        self._factories = factories

    def create(self,d):
        for f in self._factories:
            l = f.create(d)
            if l:
                return l

def Generic_Factory(clazz):
    class Anon:
        def create(self,d):
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

Room_Factory = Generic_Factory(Room)
Weapon_Factory = make_typed_factory(Weapon)
Armor_Factory = make_typed_factory(Armor)
Wand_Factory = make_typed_factory(Wands)
Character_Factory = Generic_Factory(Character)
Item_Factory = Chained_Factory([Weapon_Factory(),Armor_Factory(),Wand_Factory()])

