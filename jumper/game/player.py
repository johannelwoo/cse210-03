""" 
Player Class - This class creates the user input to have the user enter their guess for the secret word.
"""

class Player:

    def __init__(self):
        """Create the initial guess as an empty string."""
        self.letter_guess = ""

    def guess(self):
        """Get the user input for their guess of what a letter is in the secret word."""
        self.letter_guess = input("Guess a letter [a-z]: ")
        return (self.letter_guess)

    def play_again(self):
        """Get user input for whether the player wants to play again."""
        self.play_again_choice = input("Play again [y/n]? ")
        return (self.play_again_choice)

