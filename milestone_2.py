import random
def word_letter_choice():
# 1. Selection of words for game from list
 word_list = ["apple", "banana", "grape", "mango", "orange"]

# 2. Random word to be chosen from specified list
 word = random.choice(word_list)
 print(word)

# 3. Request for input from user
 guess = input ("Please select a single letter: ")

# 4. Verifying guess meets required specification
 if len(guess) == 1 and guess.isalpha():
  print("Good guess!")
 else:
  print("Oops! That is not a valid input.")

# 5. Print the letter which has been guessed
 print("The selected letter is: ", guess)

# 6. Call the function.
word_letter_choice()

