from distutils.command.clean import clean
from os import system
import requests

word_to_guess = requests.get('https://random-word-api.herokuapp.com/word').json()[0]

failed_attempts = 0
letters = []

HANGMANIMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

while failed_attempts < 7:

    letter = input("\nGuess a letter: ")
    if len(letter) > 1:
        letter = letter[0]
    current_progress = ""
    if letter.lower() in word_to_guess.lower():
        print(f"Correct! {letter} present in the word.")
        letters.append(letter)
        for letter in word_to_guess.lower():
            if letter in letters:
                current_progress += letter
            else:
                current_progress += "_"
        print(current_progress)
        if current_progress.__contains__("_") == False:
            print("You won!")
            break
    else:
        system("cls")
        print(HANGMANIMAGES[failed_attempts])
        failed_attempts += 1
        print(f"Wrong! Attempts left: {7-failed_attempts}")
print("You lost!")