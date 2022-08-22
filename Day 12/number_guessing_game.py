import imp
from art import logo
import random
SELECTED_NUMBER = random.randint(1,100)

def make_guess(guess:int):
    if guess == SELECTED_NUMBER:
        print(f"You got it! The answer was {SELECTED_NUMBER}.")
        return True
    elif guess > SELECTED_NUMBER:
        print("Too high.")
        return False
    elif guess < SELECTED_NUMBER:
        print("Too low.")
        return False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {SELECTED_NUMBER}")
attempts = 0
if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
    attempts = 10
else:
    attempts = 5



while attempts > 0:
    guess = make_guess(int(input("Make a guess: ")))
    if guess:
        exit()
    else:
        attempts -= 1
        if attempts == 0:
            print("You have run out of guesses, you lose.")
            exit()
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
