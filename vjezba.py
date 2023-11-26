#Number Guessing Game Objectives:


# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

# Include an ASCII art logo.
# from art import logo
# print (logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_answer(guess, number, turns):
  if guess > number:
    print("Too high - Try again")
    guess = int(input("Guess the number! "))
    return turns - 1
  elif guess < number :
    print("Too low - Try again")
    return turns - 1
  else :
    print(f"That's the correct number! - {number}")

#function to set difficulty
def set_diff():
  level = input("Choose level of dificulty: easy-1 or hard-2")
  if level == '1':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #random number
  number = random.randint(1,100)
  
  # Allow the player to submit a guess for a number between 1 and 100.
  turns = set_diff()
  print(f"You have {turns} attempts to guess the number")
  guess = 0
  while guess != number:
    guess = int(input("Guess the number! "))
    check_answer(guess, number, turns)
    turns = check_answer(guess, number, turns)
  #track number of turns 

game()

