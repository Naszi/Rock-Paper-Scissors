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

import random

rock_paper_scissors = [rock, paper, scissors]
your_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for  Scissors.\n"))
print(rock_paper_scissors[your_choose])
computer_choose = random.randint(0, 2)
print("Computer chose:")
print(rock_paper_scissors[computer_choose])
