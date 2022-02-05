from player import Player


class Word:

    def __init__(self):
        self.word_answer = ""
        self.word_hidden = ""
        self.guess = Player()

    def show_hidden_word(self):
        self.word_answer = self.guess
        

    def check_guess(self):
        if (self.guess == self.word_answer):
            self.word_hidden = self.guess