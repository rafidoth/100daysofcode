

print("Welcome to Tip calculator")

total_bill = float(input("What was the total bill?"))

tip = (float(input("What percentage tip would you like to give?"))/100) * total_bill

people = int(input("How many people to split bill ?"))

bill = (tip + total_bill)/people 

print(f"Each person should pay: {bill}")
