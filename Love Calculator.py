print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
lower_name = name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

score = str(true) + str(love)
int_score = int(score)

if int_score < 10 or int_score>90:
  print(f"Your score is {score}, you go together like coke and mentos")

elif int_score > 40 and int_score<50:
  print(f"Your score is {score}, you are alright together")

else: 
  print(f"Your score is {score}")

