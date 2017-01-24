import dill as pickle

from Command import Game
from create_character import create_Character




class LoadScreen:
    def menu(self):
        print("Welcome to Dragonslayers!")
        print("----------Menu-----------")
        print("1. New Game     2. Load Game     3. Quit")
        while True:
            try:
                choice = int(input("Type 1,2, or 3."))
                if choice == 3:
                    print("Thanks for playing!")
                    break
                elif choice == 1:
                    self.new_game()
                elif choice == 2:
                    filename = "data/saved/saved_game.txt"
                    with open(filename, "rb") as f:
                        foo = pickle.load(f)
                        g = Game(f)
                        g.cmdloop()
                else:
                    print("Select 1, 2, or 3.")
            except ValueError:
                print("Type 1, 2, or 3.")



    def new_game(self):
        c = create_Character()
        player = c.generate()
        g = Game(player)
        g.cmdloop()