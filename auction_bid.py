import os

def clear():
    os.system("cls")

bids = {}
bidding_finished = False

while not bidding_finished :
    name = input("What is your name?")
    price = input("What is your bid?  $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'")
    if should_continue == 'No':
        bidding_finished = True
    elif should_continue == 'Yes':
        clear() 

clear()
highest_bidder = max(bids, key = bids.get)
print(f"The winner of the auction is {highest_bidder}")