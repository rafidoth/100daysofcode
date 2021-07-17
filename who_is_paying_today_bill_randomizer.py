import random

names = input("Give everybody's name, seperated by comma.")

list_names = names.split(",")

persons = int(len(list_names))

random_person = random.randint(0, persons-1)
# zero is the lowest number and highest would be one less than the highest.

bill_payer = list_names[random_person]

print(f"Today {bill_payer} will pay our bill !!!")