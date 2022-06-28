import random
import os
from logo import logo

# function to return scores
def calculate_score(card_list):
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0
    elif score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return(score)

# function to return random cards
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# function to compare values
def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lost, dealer has blackjack!"
    elif user_score == 0:
        return "You won with a blackjack"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif dealer_score > 21:
        return "You win. Dealer went over 21."
    elif user_score > dealer_score:
        return "You win."
    else:
        return "You lose."

# function for the game itself.
def play_game():
    # defining cards and variables
    user_card = []
    dealer_card = []
    is_game_over = False

    # handing out the cards to the user and the computer.
    for _ in range(2):
        user_card.append(deal())
        dealer_card.append(deal())

    # condition for the user
    while not is_game_over:
        user_score = calculate_score(user_card)
        dealer_score = calculate_score(dealer_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's fist card: {dealer_card[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_deal == 'y':
                user_card.append(deal())
            else:
                is_game_over = True

    # condition for the dealer.
    while dealer_score !=0 and dealer_score < 17:
        dealer_card.append(deal())
        dealer_score = calculate_score(dealer_card)
    
    # final display
    print(f"Your cards are {user_card}, final score is {calculate_score(user_card)}")
    print(f"Dealer's cards are {user_card}, final score is {calculate_score(user_card)}")
    print(compare(user_score, dealer_score))


# condition for the game function to keep running
while input("Do you want to continue playing? Type 'y' or 'n':  ").lower() == "y":
    os.system('cls')
    print(logo)
    play_game()
