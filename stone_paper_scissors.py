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

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

#Write your code below this line 👇
import random
choice= int(input("What do you what to choose. Type 0 for rock, 1 for paper, 2 for scissors:"))
rand=random.randint(0,2)
if choice==rand:
  # print(rock)
  # print(scissors)
  print("Draw")
elif choice==0 and rand==1:
  print(rock)
  print(paper)
  print("You lost")
elif choice==0 and rand==2:
  print(rock)
  print(scissors)
  print("You won")
elif choice==1 and rand==0:
  print(paper)
  print(rock)
  print("You won")
elif choice==1 and rand==2:
  print(paper)
  print(scissors)
  print("You won")
elif choice==2 and rand==0:
  print(paper)
  print(rock)
  print("You lost")
elif choice==2 and rand==1:
  print(scissors)
  print(paper)
  print("You won")
  
  
