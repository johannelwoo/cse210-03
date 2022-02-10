
from game.player import Player
from game.drawing import Drawing
from game.word import Word

import random

class Host:
    """ 
    Host Class
    Purpose: To manage the game by selecting a word, drawing the jumper and asking the player to guess the word a letter at a time.  
             If the guessed letter is not in the word, part of the parachute is removed. If the word is guessed before the patachute 
             disappears, the player wins. if not, the player loses.
        
    Attributes/purpose
	    listofwords
    	player
	    drawing

    Methods/purpose
	    create_wordlist()
	    play_game()
    """

    def __init__(self):
        # __init__ is a constuctor that initializes the class attributes
        self._wordlist_of_words = []
        self.player = Player()
        self.drawing = Drawing()
        self.word = Word("")

    def create_wordList(self):
        # This method establishes a wordlist from which a word is chosen at random.
        self._wordlist_of_words = [
            Word('developement'), 
            Word('python'), 
            Word('student'), 
            Word('arguments'), 
            Word('teamwork'), 
            Word('encapsulate'), 
            Word('abstract'), 
            Word('jumper'), 
            Word('cooperation'), 
            Word('variable'), 
            Word('method'), 
            Word('classes'), 
            Word('objects'), 
            Word('program')
            ]
        return random.choice(self._wordlist_of_words)

    def play_game(self):
        # This method plays the game.  It loops until the game is won or lost and loops while the player wants to keep playing.
        self.word = self.create_wordList()
        play_again = "y"

        while play_again == "y":
            game_over = False
            while not game_over:
                self.drawing.print_parachute()
                self.drawing.print_person()
                self.word.show_hidden_word()
                guessed_correctly = self.word.check_guess(self.player.guess())
                if (not guessed_correctly):
                    game_over = self.drawing.remove_parachute()
                if game_over:
                    print("\nOh no!  Your parachute is gone!  You lose!")
                    self.drawing.kill_person()
                    print("The word was:")
                    self.word.show_word()
                if (self.word.is_word_completely_guessed()):
                    print("\nCongratulations!  You guessed the word!\n")
                    print("The word was:")
                    self.word.show_hidden_word()
                    print("\n")
                    game_over = True           
            play_again = self.player.play_again()
            if play_again == "y":
                self.drawing.reset_drawing()
                self.word = random.choice(self._wordlist_of_words)
           
        
        
        