

class Word: 
 
    def __init__(self, random_word):
                
        self.letters = []
        self._word_hidden = []
        self.word_completely_guessed = False
        
        #make a list of letters from the random word
        for letter in random_word:
            self.letters.append(letter)
        #take the list of letters from the random word and makes a list of underscore
        for letter in self.letters:
            letter = "_"
            #stablish a list of underscore with no commas.
            self._word_hidden.append(letter)
    
    def is_word_completely_guessed(self):
        return(self.word_completely_guessed)

    def show_hidden_word(self): 
        #Put the hidden word inside the variable word and display that
        word = ""
        for letter in range(len(self._word_hidden)):
            word += self._word_hidden[letter]
        print(word)               

    def check_guess(self, guess):
        #take a parametrer and use it to check if the guess word is in the letters list
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

