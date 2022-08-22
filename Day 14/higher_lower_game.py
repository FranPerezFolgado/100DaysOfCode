from multiprocessing.spawn import import_main_path
from art import logo, vs
from game_data import data
import random
import os


def clear_console():
    os.system('clear')
    print("\n" + logo)


score = 0
def game(score:int, choice_a):
    clear_console()
    if score > 0:
        print(f"You're right! Current score: {score}")
    else:
        choice_a = random.choice(data)
    choice_b = random.choice(data)
    while choice_a == choice_b:
        choice_b = random.choice(data)

    print("Compare A: " + str(choice_a["name"] + ", " + choice_a["description"] + ", from " + choice_a["country"]))
    print(vs)
    print("Against B: " + str(choice_b["name"] + ", " + choice_b["description"] + ", from " + choice_b["country"]))
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    def check_choice(choice:str):
        if choice_a["follower_count"] > choice_b["follower_count"]:
            return choice == "a"
        else:
            return choice == "b"
    clear_console()
    if check_choice(choice):
        score += 1
        game(score, choice_b)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

game(score, None)