import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
plays = [rock, paper, scissors]

play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors." ))
computer_play = random.randint(0,2)
print(plays[computer_play] + "\n\nVS\n\n" + plays[play])
if play == 0 and computer_play == 1:
    print("Sorry, you lose!")
elif play == 1 and computer_play == 2:
    print("Sorry, you lose!")
elif play == 2 and computer_play == 0:
    print("Sorry, you lose!")
elif play == computer_play:
    print("DRAW!")
else:
    print("You win!")