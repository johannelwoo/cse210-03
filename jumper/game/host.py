# New game
from game.player import Player
from game.drawing import Drawing
from game.word import Word

import random

class Host:
    """ Purpose: To manage the game by selecting a work, draying the jumper and asking the player for guesses
Attributes/purpose
	listofwords
	player
	drawing
Methods/purpose
	create_wordlist()
	play_game()"""

    def __init__(self):
        self._wordlist_of_words = []
        self.player = Player()
        self.drawing = Drawing()
        self.word = Word()

    def create_wordList(self):
        self._wordlist_of_words = ['developement', 'python', 'hilo', 'arguments', 'program']
        return random.choice(self._wordlist_of_words)
    def play_game(self):
        #print(self.word.show_hidden_word(self.create_wordList()))
        cont = 0
        word = self.word.show_hidden_word(self.create_wordList())
        while cont <= 8:    
            letter = self.word.check_guess(self.player.guess())
            letter_show = []
            for i in range(len(word)):
                if(word.find(letter) != -1):
                    if(word[i] == letter):
                        letter_show.append(letter)
                    else:
                        letter_show.append("_")
                else:
                    cont += 1
                    
            print(letter_show)  
            
        return print(letter_show)
           
        
        
        