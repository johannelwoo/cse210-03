# This ones me

# drawing array/list

# draw()
# wrong_guess()


# from player import *
# from word import *


class Drawing():
    def __init__(self):
        self.parachute = '   ___\n  /___\\\n  \\   /  \n   \\ /'
        self.person = ('    O  \n   /|\\  \n   / \\')
        
    def print_parachute(self):
        # self.parachute = (' ___\n/___\\\n\\   /\n \\ /')
        print(self.parachute)
        
    def remove_parachute(self):
        self.parachute = self.parachute[7:]
        if len(self.parachute) <= 15:
            self.parachute = self.parachute[4:]
        # print(self.parachute)
        # print(self.person)
        
    def print_person(self):
        print(self.person)
        
    def kill_person(self):
        self.person = ('    x\n   /|\\\n   / \\')
