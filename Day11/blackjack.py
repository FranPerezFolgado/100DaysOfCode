from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_cards(num_of_cards, list: list):
    for i in range(0, num_of_cards):
        list.append(random.choice(cards))
    return list

def has_blackjack(list: list):
    list_copy = list.copy()
    if sum(list_copy) == 21:
        return True
    elif list_copy.__contains__(11):
        list_copy[list_copy.index(11)] = 1
        if sum(list_copy) == 21:
            return True
    
    return False

def calculate_score(list:list):
    score = sum(list)
    if list.__contains__(11) and sum(list) > 21:
        list[list.index(11)] = 1
        score = sum(list)
    return score


def check_win(user_cards:list, computer_cards:list, another_card: bool):
    if has_blackjack(computer_cards) or calculate_score(user_cards) > 21:
        print("The computer won")
        return True
    elif has_blackjack(user_cards) and not has_blackjack(computer_cards) or calculate_score(computer_cards) > 21:
        print("You won!")
        return True
    elif not another_card:
        if calculate_score(user_cards) >  calculate_score(computer_cards):
            print("You won!")
            return True
        elif calculate_score(user_cards) < calculate_score(computer_cards):
            print("The computer won")
            return True
        else:
            print("Draw!")
            return True
    else:
        print("Another round")
        return False

def computer_play(computer_cards:list):
    if calculate_score(computer_cards) < 16:
        computer_cards = pick_cards(1,computer_cards)
        computer_play(computer_cards)
    else:
        return computer_cards


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
    print(logo)
    user_cards = []
    user_cards = pick_cards(2,user_cards)
    computer_cards=[]
    computer_cards = pick_cards(2,computer_cards)
    user_score = calculate_score(user_cards)
    if check_win(user_cards,computer_cards, True):
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score {user_score}")
        print(f"Computer's cards: {computer_cards}, current score {computer_score}") 
        exit()
        
 
    another_card = True
    while another_card:
        print(f"Your cards: {user_cards}, current score {user_score}")
        print("Computer's first card: " + str(computer_cards[0])) 
        another_card_response = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card_response == 'y':
            user_cards = pick_cards(1,user_cards)
            user_score = calculate_score(user_cards)
        elif another_card_response != 'y':
            another_card = False
            computer_play(computer_cards)

        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score {user_score}")
        print(f"Computer's cards: {computer_cards}, current score {computer_score}") 
        if check_win(user_cards,computer_cards, another_card):
            exit()
        

else:
    exit()