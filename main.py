# Rock paper scissors game starts...
import random

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________) 
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper, Scissor game !!")
# user_input = input("Enter one number, \n1 - Rock, \n2 - Paper, \n3 - Scissor\n")
random_var = random.randint(1,3)
print(random_var)
user_input = int(input("Please select one number,\n1.Rock\n2.Paper\n3.Scissor\n"))
if user_input == random_var:
    print("no one wins !!")
elif user_input==1 and random_var==3:
    print("You won the match")
elif user_input==2 and random_var==1:
    print("You won the match")
elif user_input==3 and random_var==2:
    print("You won the match")
else:
    print(" Sorry you lost the match,")



