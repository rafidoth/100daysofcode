name = input("What is your name ? ")
user_input = input("Enter 0 for rock, 1 paper, 2 for scissors\n")

#rock =0 paper = 1 scissors=2
import random
computer_input = random.randint(0,2) 

print(computer_input)

if user_input == 0 and computer_input == 2:
  print(f"{name} won")

elif user_input == 2 and computer_input == 1:
  print(f"{name} won")

elif user_input == 1 and computer_input == 0:
  print(f"{name} won")  

elif user_input == computer_input:
  print(f"match draw")

else:
  print("Your lost")
