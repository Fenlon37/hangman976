# 1. Importing random module.
import random

# 2. Creating word list and selecting word from list for game.
word_list = ["apple", "banana", "grape", "mango", "orange"]
word = random.choice(word_list)

# 3. Creating function to check that the guess made is within the word.
def check_guess(guess):
 guess=guess.lower()
 if guess in word:
  print(f"Good guess! '{guess}' is in the word.")
 else:
  print(f"Sorry, '{guess}' is not in the word. Try again.")

# 4. Creating while loop to ask for input of letter and checking that it is valid.
def ask_for_input():
  while True:
   guess = input("Guess a letter: ")
   if len(guess) == 1 and guess.isalpha():
    check_guess(guess)
    break
   else:
    print("Invalid letter. Please, enter a single alphabetical character.") 

# 5. Calling function to recieve letter input from user.
ask_for_input()
