import textwrap

class Game_Screen():
    def __init__(self, message):
        self.message = message

    """Prints the received message to the user."""
    def print_screen(self,message):
        for line in textwrap.wrap(message, 72):
            print(line)

    def clearScreen(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')



