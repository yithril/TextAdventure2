class Gold:
    def do(self, state):
        gold = state.player.get_gold()
        print("You have "+str(gold)+" gold pieces.")
