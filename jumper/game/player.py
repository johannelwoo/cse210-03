
class Player:

    def __init__(self):
        self.letter_guess = ""

    def guess(self):
        self.letter_guess = input("Guess a letter [a-z]: ")
        return (self.letter_guess)

