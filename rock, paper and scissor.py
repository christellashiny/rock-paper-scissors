Human_Input=int(input(" what do you choose? Type 0 for rock,1 for paper or 2 for scissors "))
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

if Human_Input < 0 or Human_Input > 2:
    print("Invalid input")
else:
    if Human_Input == 0:
        print(rock)
    elif Human_Input == 1:
        print(paper)
    else:
        print(scissors)

    computer_Input = random.randint(0, 2)

    if computer_Input == 0:
        print("Computer chooses:", rock)
    elif computer_Input == 1:
        print("Computer chooses:", paper)
    else:
        print("Computer chooses:", scissors)

    if Human_Input == computer_Input:
        print("Draw")
    elif Human_Input == 1 and computer_Input == 0:
        print("Player wins")
    elif Human_Input == 2 and computer_Input == 1:
        print("Player wins")
    elif Human_Input == 0 and computer_Input == 2:
        print("Player wins")
    else:
        print("Computer wins")

