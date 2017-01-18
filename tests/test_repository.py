from factory import Weapon_Factory, Room_Factory
from file_loader import File_Loader
from repository import Repository
from Weapon import Weapon


def test_repository():
    loader = File_Loader("data/items/")
    factory = Weapon_Factory()
    repository = Repository(loader, factory)
    test_case = repository.get_by_id(1)
    weapon = Weapon(name="iron longsword",
                    desc="A short, decently constructed iron longsword.",
                    long_desc="This longsword does not feel too heavy.  The blade is somewhat rusted on the edges, and the sides are not as keen as they could be.",
                    weight=8,
                    value=30,
                    can_pick_up="True",
                    is_magical="False",
                    is_cursed="False",
                    type = "Weapon",
                    handed=1,
                    offhand=0,
                    weapon_type="longsword",
                    const_damage=0,
                    damage_hit_dice=6,
                    damage_hit_dice_coefficient=1,
                    damage_stat="strength",
                    damage_type="slashing",
                    keywords = [])
    assert test_case == weapon

