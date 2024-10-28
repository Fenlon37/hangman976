import random

class hangman:
 """
 Class of the hangman game
 """
 def __init__(self, word_list, num_lives=5):
  """
  The hangman game will have the parameters of word_list and num_lives initialised.
  """
  self.word_list = word_list
  self.num_lives = num_lives

  self.word = random.choice(self.word_list)
  
  self.word_guessed = ['_' for _ in self.word]
  self.num_letters = len(set(self.word))
  self.list_of_guesses = []
 """
 Creating function to check that the guess made is within the word and calculating lives left.
 """
 def check_guess(self, guess):
  guess=guess.lower()
  if guess in self.word:
   print(f"Good guess! '{guess}' is in the word.")
   for index, letter in enumerate(self.word):
    if letter == guess:
     self.word_guessed[index] = guess
  else:
    self.num_lives -= 1 
    print(f"Sorry, {guess} is not in the word.")
    print(f"You have {self.num_lives} lives left.")

 """
 Creating while loop to ask for input of letter and checking that it is a valid and not previously tried.
 """
 def ask_for_input(self):
  while True:
   guess = input("Guess a letter: ")
   if len(guess) != 1 or not guess.isalpha():
    print("Invalid letter. Please, enter a single alphabetical character.")
   elif guess in self.list_of_guesses:
    print("You already tried that letter!")
   else:
    self.check_guess(guess)
    self.list_of_guesses.append(guess)
    break
   ask_for_input(self)

if __name__ == "__main__":
 word_list = ["Apple", "Banana", "Grape", "Mango", "Orange"]
 game = hangman(word_list)
 game.ask_for_input()

 print("Word guessed so far:", game.word_guessed)
 print("List of guesses:", game.list_of_guesses)
 print("Lives remaining:", game.num_lives)
