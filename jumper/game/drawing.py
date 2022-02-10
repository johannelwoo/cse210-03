"""
Class Drawing and all its encapsulated attributes and methods
"""

class Drawing():
    """ The Drawing class handles all functionality having to do with the drawing of the man and the parachute"""
    def __init__(self):
        # __init__ initializes the drawing
        self.parachute = ('\n    ___ \n   /___\\\n   \\   /\n    \\ / ')
        self.person = ('     O  \n    /|\\  \n    / \\\n\n^^^^^^^^^^^')

    def reset_drawing(self):
        # reset the drawing if the player chooses to play again
        self.parachute = ('\n    ___ \n   /___\\\n   \\   /\n    \\ / ')
        self.person = ('     O  \n    /|\\  \n    / \\\n\n^^^^^^^^^^^')
        
    def print_parachute(self):
        # This method prints the parachute part of the drawing when called.
        print(self.parachute)
        
    def print_person(self):
        # This method prints the person portion of the drawing
        print(self.person)

    def kill_person(self):
        # This method changes the person portion of the drawing to a person falling with birds floating and then it prints the person.
        self.person = ("\n\n    \\x/   ~\n ~  \\|/  \n      \n\n^^^^^^^^^^^")
        self.print_person()

    def remove_parachute(self):
        # This method removes parts of the parachute drawing when an incorrect letter is guessed.
        parachute_gone = False
        self.parachute = self.parachute[9:]
        if len(self.parachute) == 0:
            parachute_gone = True
        return(parachute_gone)
      
