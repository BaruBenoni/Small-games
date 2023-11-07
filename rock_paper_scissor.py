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

#Write your code below this line 
import random
choice=int(input("Welcome to the Game! Which one do you chose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
symbol=[rock, paper, scissors]
if choice <0 or choice >2:
  print("Invalid number. You lose.")
else:
  print(f"{symbol[choice]}")
random_symbol=random.randint(0,2)
print(f"Computer chose: {symbol[random_symbol]}")

if choice==0 and random_symbol==2:
  print("You win.")
elif choice==1 and random_symbol==0:
  print("You win.")
elif choice==2 and random_symbol==1:
  print("You win.")
  
elif choice==2 and random_symbol==0:
  print("You lose.")
elif choice==0 and random_symbol==1:
  print("You lose.")
elif choice==1 and random_symbol==2:
  print("You lose.")  
else:
  print("Draw.")
