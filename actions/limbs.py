from collections import OrderedDict

class LimbsAction:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def do(self,state):
        base = OrderedDict()
        base["Main Hand"] = state.player.race.get_body_slot("Main Hand")
        base["Off Hand"] = state.player.race.get_body_slot("Off Hand")
        base["Head"] = state.player.race.get_body_slot("Head")
        base["Neck"] = state.player.race.get_body_slot("Neck")
        base["Body"] = state.player.race.get_body_slot("Body")
        base["Back"] = state.player.race.get_body_slot("Back")
        base["Waist"] = state.player.race.get_body_slot("Waist")
        base["Hands"] = state.player.race.get_body_slot("Hands")
        base["Feet"] = state.player.race.get_body_slot("Feet")
        base["Ring Slot 1"] = state.player.race.get_body_slot("Ring Slot 1")
        base["Ring Slot 2"] = state.player.race.get_body_slot("Ring Slot 2")
        base["Bag Slot"] = state.player.race.get_body_slot("Bag Slot")
        for value, key in base.items():
            if key == 0:
                equipment_slot = "Empty"
            else:
                equipment_slot = self.item_repository.get_by_id(key).get_name()
            print("[{0}] : [{1}]".format(value, equipment_slot.title()))
