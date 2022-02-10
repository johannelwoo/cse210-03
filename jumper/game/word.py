"""
Word Class encapulates all attributes and methods needed to handle the word in this jumper Game
"""

class Word: 
 
    def __init__(self, random_word):
        # __init__ contructor is the method that initializes all attributes
                
        self.letters = []
        self._word_hidden = []
        self.word_completely_guessed = False
        
        #make a list of letters from the random word
        for letter in random_word:
            self.letters.append(letter)
        #take the list of letters from the random word and makes a list of underscore
        for letter in self.letters:
            letter = "_"
            #stablish a list of underscores to match the word.
            self._word_hidden.append(letter)
    
    def is_word_completely_guessed(self):
        # This method lets the Host know that the word has been completely guessed.
        return(self.word_completely_guessed)

    def show_hidden_word(self): 
        # Display the hidden word
        word = "\n"
        for letter in range(len(self._word_hidden)):
            word += self._word_hidden[letter]
        print(word)               
        print()

    def show_word(self): 
        # Display the word the player has been trying to guess
        word = "\n"
        for letter in range(len(self.letters)):
            word += self.letters[letter]
        print(word)               
        print()

    def check_guess(self, guess):
        #take the letter passed as a parameter and see if it is in the hidden word
        guessed_correctly = False
        position = 0
        for i in self.letters:
            if i == guess:
                self._word_hidden[position]=guess
                guessed_correctly = True
            position += 1

        position = 0
        self.word_completely_guessed = True
        for i in self._word_hidden:
            if i == "_":
                self.word_completely_guessed = False
            position += 1
        return (guessed_correctly)

