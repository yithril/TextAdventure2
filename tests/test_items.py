import pytest

from items import Items


def test_if_cannot_pick_up():
    sword = Items(id=1, name="rock", desc="a rock", long_desc="a rock", weight=2, value=1, can_pick_up= "True",
                  is_magical="True", is_cursed="False", keywords=["pebble"], type="Item")
    sword2 = Items(id=2, name="rock", desc="a rock", long_desc="a rock", weight=4, value=1, can_pick_up= "False",
                   is_magical="True", is_cursed="False", keywords=["pebble"], type="Item")
    assert sword.get_can_pick_up() == "True"
    assert sword2.get_can_pick_up() == "False"
