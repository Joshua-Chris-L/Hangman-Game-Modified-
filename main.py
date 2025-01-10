# Hagmann Game
from hangman_words import hangman_words 
from hangmannArtIntro import hangman
from hangman_art import HANGMANPICS
import random


#Choose a word from the guess word
print(hangman)
random_word = random.choice(hangman_words)
len_word = len(random_word)

#Print a welcome message
print(f"You are welcome to the hangmann game. You are to guess\
 a word. The word has {len_word} alphabet. It begins with {(random_word[0]).upper()} and ends with {(random_word[-1]).upper()}.")

#Modified Hangman Game Sequence
placeholder = ""
for word in range(0, len(random_word)):
    num_of_trial = len_word - word
    print(f"You have {num_of_trial} trials left")
    guess_word = input("Enter your guess: ").lower()
    if guess_word == "":
        placeholder +="_"
        print(HANGMANPICS[-1]) if word == random_word[-1] else print(HANGMANPICS[word])
        print("You have enterd an incorrect guess")
    elif guess_word in random_word:
        placeholder += guess_word
        print("You have entered a correct guess")
    else:
        placeholder +="_"
        print(HANGMANPICS[-1]) if word == random_word[-1] else print(HANGMANPICS[word])
        print("You have enterd an incorrect guess")

#Get length of correct and length of incorrect words
correct_words = 0
incorrect_words = 0
for word in placeholder:
    if word == "_":
        incorrect_words +=1
    else:
        correct_words +=1

#Print Game Results
print(placeholder)
if correct_words == len(random_word):
    print(f"You won the hangman game \U0001F600. My initial guess word was {(random_word).upper()}")
else:
    print(f"You got {correct_words} words correct \U0001FAE0 . My initial guess word was \
{(random_word).upper()} You lose !!! {HANGMANPICS[-1]}")