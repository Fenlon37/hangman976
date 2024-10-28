import random

class Hangman:
 '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game.
    num_lives: int
        Number of lives the player has.
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list.
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed.
        If the word is 'mango', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['_', 'a', '_', '_', '_']
    num_letters: int
        The number of letters in the word that have not been guessed yet.
    num_lives: int
        The number of lives the player has left.
    list_letters: list
        A list of the letters that have already been tried.

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
 
 def __init__(self, word_list, num_lives=5):  # Initiating the variables.
  self.word_list = word_list
  self.num_lives = num_lives
  self.word = random.choice(word_list).lower()
  self.word_guessed = ['_' for _ in self.word]
  self.num_letters = len(set(self.word))
  self.list_letters = []
  print(f"The mystery word has {len(self.word)} characters")
  print(" ".join(self.word_guessed)) # Printing list of letters together when a letter is guessed correctly.
 
 def check_letter(self, letter):
  '''
  Checks if the letter is in the word.
  If it is, it replaces the '_' in the word_guessed list with the letter.
  If it is not, it reduces the number of lives by 1.

  Parameters:
  ----------
  letter: str
    The letter to be checked
  ''' 
  letter=letter.lower()
  if letter in self.word:
    print(f"Good guess! '{letter}' is in the word.")
    for index, char in enumerate(self.word): # Will track position of letter guessed in word.
     if char == letter:
      self.word_guessed[index] = letter
    self.num_letters -= 1 
  else:
    self.num_lives -= 1 
    print(f"Sorry, {letter} is not in the word.")
    print(f"You have {self.num_lives} lives left.")
  print(" ".join(self.word_guessed))
 """
 Creating while loop to ask for input of letter and checking that it is a valid and not previously tried.
 """
 def ask_letter(self):
  '''
  Asks the user for a letter and checks two things:
  1. If the letter has already been tried
  2. If the character is a single character
  If it passes both checks, it calls the check_letter method.
  '''
  while True:
   letter = input("Please guess a letter: ").lower()
   if len(letter) != 1 or not letter.isalpha(): # Checks if more than one letter submitted together or if not a letter.
    print("Invalid letter. Please, enter just one character.")
   elif letter in self.list_letters: # Checks if letter has already been tried within the history of the game.
    print(f"{letter} was already tried")
   else:
    self.check_letter(letter)
    self.list_letters.append(letter) # Adds letter to list of letters that have been tried
    break

def play_game(word_list):
 num_lives = 5
 game = Hangman(word_list, num_lives=5)
 while True:
  if game.num_lives == 0:
   print(f"You lost! The word was {game.word}")
   break
  elif game.num_letters > 0:
   game.ask_letter()
  else:
   print("Congratulations. You won the game!")
   break 

if __name__ == "__main__": # Allows the game to function only when the script is directly executed.
 word_list = ["apple", "banana", "grape", "mango", "orange"]
 play_game(word_list)
