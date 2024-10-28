# Hangman
## Table of Contents
- [Project Description](#project-description)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [License](#license)

## Project Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game using python, where the game randomly selects a word from a pre-defined list and the user tries to guess it before they run out of lives. 


**Aim of the project**:
- Utilise python techniques and concepts including lists, loops, functions, classes and conditional statements in Python.
- Practice taking user input and verifying its validity.
- Create a console-based game within python.
- Gain experience in version control using Git and GitHub.

**What I learned**:
- Basics of Git and GitHub for version control.
- Using Python's *'random'* module and *'input ()'* function.
- Writing modular code through the use of functions and classes.
- Error handling with *'if'*, *elif* and *'else'* statements.
  
## Installation Instructions
To run the project locally, follow these steps:
1. Clone the repository: git clone https://github.com/Fenlon37/hangman976.git
2. Navigate to the project directory using the *cd* command.
3. Make sure python (3.6 or later) is installed using the *python --version* command.
4. Run the python game script *python milestone_5.py*.

## Usage instructions
1. The script will be run providing a random name from a predefined list.
2. The user will try to guess the word by inputting a letter of their choice until they are out of lives.
3. The program will validate the user input to check selection is valid.
4. If valid, the program will determine whether the letter is within the selected word.
5. The user starts with 5 lives and will lose one for each incorrect attempt.
6. Should the word be guessed, or the user have used all of their attempts, the game will end and the outcome will be provided to the user.

### File structure
Hangman game                         
1. milestone_1.py                       
- Initial script for Hangman logic and letter validation
2. milestone_2.py                        
- Refined code with basic game loops and feedback
3. milestone_3.py                      
- Script adding letter and word checking methods
4. milestone_4.py                   
- Script with class-based refactoring and complete gameplay
5. milestone_5.py               
- Final script for running the game
6.  README.md  
### Licence
This project is licensed under the MIT License. You are free to use, modify, and distribute this code, as long as proper credit is given.
