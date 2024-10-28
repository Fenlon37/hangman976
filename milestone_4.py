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
   self.num_letters -= 1
  else:
   self.num_lives -= 1 
   print(f"Sorry, {guess} is not in the word.")
   print(f"You have {self.num_lives} lives left.")
  print(" ".join(self.word_guessed))

 """
 Creating while loop to ask for input of letter and checking that it is a valid and not previously tried.
 """
 def ask_for_input(self):
  while True:
   guess = input("Guess a letter: ").lower()
   if len(guess) != 1 or not guess.isalpha():
    print("Invalid letter. Please, enter a single alphabetical character.")
   elif guess in self.list_of_guesses:
    print("You already tried that letter!")
   else:
    self.list_of_guesses.append(guess)
    self.check_guess(guess)
    break
"""
Testing that the game works
"""
if __name__ == "__main__":
    word_list = ["apple", "banana", "grape", "orange", "mango"]
    game = hangman(word_list)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()
    
    if game.num_lives == 0:
        print(f"You lost! The word was '{game.word}'.")
    else:
        print("Congratulations! You won!")

