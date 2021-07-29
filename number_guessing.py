import random


def guess_num():
    return random.randint(1, 100)

def level_define():
    n= input("Difficulty level = 'easy' or 'hard'")
    if n == 'easy':
        return 10
    elif n == 'hard':
        return 5

def game():
    num = guess_num()
    attempts = level_define()
    should_stop = False

    while should_stop == False:
        user_in = int(input("Guess a number"))
        attempts -= 1
        if attempts > 0 :
            if user_in > num:
                print("Your guess is greater than the number")
                should_stop = False
            elif user_in < num:
                print("Your guess is lower than the number")
                should_stop = False
            elif user_in == num:
                print("Your guess is right")
                should_stop = True

            print(f"attempts:{attempts}")
        else:
            should_stop = True
            print("Your attempts are over. You lost. The number was{num}")



print("Welcome to the number guessing game.")
game()