# Important Points: IF computer or user any of them has a blackjack(Ace + 10 card) = Win If ace is given to someone,
# it will be counted as 11 but if the total after counting is more than 21 then Ace will be counted as 1 If anyone's
# score is more than 21 then immediately he will loss


# required things
import random
import os  # clear for cleaning the screen


# Functions


def random_hit():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_scores, comp_scores):
    if user_scores == comp_scores:
        return "Draw😶"
    elif comp_scores == 0 :
        return "Lose, opponent has Blackjack"
    elif user_scores== 0 :
        return  "Win with a Blackjack"
    elif user_scores>21:
        return "You went over. You lose."
    elif comp_scores>21:
        return "Opponent wen over. You win."
    elif user_scores > comp_scores:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    is_game_over = False
    # first hit which is random
    comp_cards = []
    user_cards = []

    for _ in range(2):
        user_cards.append(random_hit())
        comp_cards.append(random_hit())



    while not is_game_over:
        user_scores = calculate_score(user_cards)
        comp_scores = calculate_score(comp_cards)
        print(f"       Your cards: {user_cards}, current score: {user_scores}")
        print(f"       Computer's first card: {comp_cards[0]}")
        if user_scores == 0 or comp_scores == 0 or user_scores > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(random_hit())
            else:
                is_game_over = True

    while comp_scores != 0 and comp_scores < 21 :
        comp_cards.append(random_hit())
        comp_scores = calculate_score(comp_cards)

    print(compare(user_scores, comp_scores))

###########

while input("Do you want to play a game of Black jack? Type 'y' or 'n'") =='y':
    play_game()



















