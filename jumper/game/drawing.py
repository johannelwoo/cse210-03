# This ones me

# drawing array/list

# draw()
# wrong_guess()


# from player import *
# from word import *


class Drawing():
    def __init__(self):
        self.parachute = ('\n    ___ \n   /___\\\n   \\   /\n    \\ / ')
        self.person = ('     O  \n    /|\\  \n    / \\\n\n^^^^^^^^^^^')

    def reset_drawing(self):
        # reset the drawing if the player chooses to play again
        self.parachute = ('\n    ___ \n   /___\\\n   \\   /\n    \\ / ')
        self.person = ('     O  \n    /|\\  \n    / \\\n\n^^^^^^^^^^^')
        
    def print_parachute(self):
        # self.parachute = ('\n ___\n/___\\\n\\   /\n \\ /')
        print(self.parachute)
        
    def remove_parachute(self):
        parachute_gone = False
        self.parachute = self.parachute[9:]
        if len(self.parachute) == 0:
            parachute_gone = True
        return(parachute_gone)
      
    def print_person(self):
        print(self.person)
        
    def kill_person(self):
        self.person = ("\n\n    \\x/   ~\n ~  \\|/  \n      \n\n^^^^^^^^^^^")
        self.print_person()
