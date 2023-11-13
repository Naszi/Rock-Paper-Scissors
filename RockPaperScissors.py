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

rock_paper_scissors = [rock, paper, scissors]
your_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for  Scissors.\n"))
if your_choose >= 3 or your_choose < 0:
    print("You typed an invalid number, You lose!")
else:
    computer_choose = random.randint(0, 2)
    print(rock_paper_scissors[your_choose])
    print("Computer chose:")
    print(rock_paper_scissors[computer_choose])
    if your_choose == 0 and computer_choose == 2:
        print("You Win!")
    elif computer_choose == 0 and your_choose == 2:
        print("You lose!")
    elif your_choose > computer_choose:
        print("You win!")
    elif computer_choose > your_choose:
        print("You lose!")
    elif computer_choose == your_choose:
        print("It's draw.")