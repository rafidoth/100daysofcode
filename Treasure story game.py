print("Welcome to the treasure story game")

dcsn = input("What will you choose? Left or Right ???")

if dcsn == "Left":
    dcsn_2 = input("There is a river out there. Will you swim or wait?")
    if  dcsn_2 == "swim":
        print("Game Over")
    else:
        dcsn_3 = input("There are three doors. which one you'll open??? Red, blue, Yellow")

        if dcsn_3 == "Yellow":
            print("You won") 
        if dcsn_3 == "Red" or dcsn_3 == "blue":
            print("Game Over")
            
else:
    print("Game Over")  