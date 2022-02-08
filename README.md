# cse210-03 assignment

 Jumper Game 

 A game where the play must guess the letters of a word.  The player starts with a full parachute.  If they guess correctly, the letter is revealed within the word.  If they guess incorrectly, a part of the parachute is removed.  If they guess the entire word before the parachute is gone, they win.  If not, they lose.

 Specifications

 The puzzle is a secret word randomly chosen from a list.
 The player guesses a letter in the puzzle.
 If the guess is correct, the letter is revealed.
 If the guess is incorrect, a line is cut on the player's parachute.
 If the puzzle is solved the game is over.
 If the player has no more parachute the game is over.

# Files

host.py
player.py
word.py
drawing.py

# Classes

Class 1 (principal class)
Name: Host 
Purpose: To manage the game by selecting a work, draying the jumper and asking the player for guesses

Attributes/purpose
  listofwords - contains a list of Word objects, each with a word to guess
  player - contains a Player
  drawing - contains a Drawing

Methods/purpose
  create_wordlist() - create a list of Word objects
  play_game() - execute the game

Class 2
Name: Word
Purpose: To contain the word to be guessed and the progress being made in guessing the word.  This class will also identify that the word has been guessed.	 

Attributes/purpose
  word_answer - contains the word the player is trying to guess
  word_hidden - contains the word the player has guessed so far.  
  When these two words match, the player has won

Methods/purpose
  show_hidden_word() - print the word the player has guessed so far to the console.
  check_guess(letter) - determine if the guessed letter matches a letter in the word_answer.  If so, reveal that letter in the hidden word.

Class 3
Name: Drawing
Purpose:  This class contains all the information about the drawing and provides the function that prints the drawing.

Attributes/purpose
  drawing - contains the drawing of the man on the parachute

Methods/purpose
  draw() - print the drawing of the parachute to the console
  wrong_guess() - this gets called if the guess is wrong.  It removes a piece of the parachute from the drawing.

Class 4
Name: Player
Purpose: This class contains information about the player.  It specifically asks the player what their guess is.

Attributes/purpose
  None

Methods/purpose
  guess() - Asks the player for his/her guess and returns it.


# Team

Alexander Calva
Mark Richmond
Johanna Schick
Jake Soulier
Didier Virguez


