

class Word: 
 
    def __init__(self):
                
        self.letters = []
        self._word_hidden = []

    def rand_word_list(self, random_word):
        #make a list of letters from the random word
        for letter in random_word:
            self.letters.append(letter)


    def underscore(self):
        #take the list of letters from the random word and makes a list of underscore
        for letter in self.letters:
            letter = "_"
            #stablish a list of underscore with no commas.
            self._word_hidden.append(letter)

    def show_hidden_word(self): 
        #Put the hidden word inside the variable word and display that
        word = ""
        for letter in (len(self._word_hidden)):
            word += self._word_hidden[letter]

        print(word)               

    def check_guess(self, guess):
        #take a parametrer and use it to check if the guess word is in the letters list
        for letter in self.letters:
            if letter in guess:
                self._word_hidden = letter
            else:
                self._word_hidden = "_"
