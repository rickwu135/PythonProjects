############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
cpu_hand = []


def draw():
    """"Draw a random card from cards"""
    return random.choice(cards)


def calculate_score(hand):
    """Calculates the score of your hand"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(user_score, cpu_score):
    """Compares the hands of cpu and user and declares the winner"""
    if user_score == cpu_score:
        print("It's a draw")
    elif cpu_score == 0:
        print("CPU Wins")
    elif user_score == 0 and cpu_score != 0:
        print("User Wins")
    elif user_score > 21:
        print("User Loses")
    elif cpu_score > 21:
        print("CPU Loses")
    elif user_score > cpu_score:
        print("User Wins")
    else:
        print("CPU Wins")


def play():
    """Starts the game"""
    game_over = False
    print(art.logo)
    for i in range(2):
        user_hand.append(draw())
        cpu_hand.append(draw())

    user_score = calculate_score(user_hand)
    cpu_score = calculate_score(cpu_hand)

    print(f"{user_hand}, current score: {user_score}")
    print(f"CPU first card: {cpu_hand[0]}")
    while not game_over:
        if user_score == 0 or cpu_score == 0 or user_score > 21:
            game_over = True
        if input("Do you want to draw again?: ") == 'yes':
            user_hand.append(draw())
            user_score = calculate_score(user_hand)
            print(user_hand)
            print(user_score)
            if user_score == 0 or cpu_score == 0 or user_score > 21:
                game_over = True
        else:
            game_over = True
    print("CPU Turn: ")
    cpu_t = True
    while cpu_t:
        print(cpu_hand)
        print(cpu_score)
        if cpu_score > 17 or cpu_score == 0:
            cpu_t = False
        elif cpu_score <= 17:
            cpu_hand.append(draw())
            cpu_score = calculate_score(cpu_hand)

    compare(user_score, cpu_score)
    print(f"Final Hand for User: {user_hand} Final Score: {user_score}")
    print(f"Final Hand for CPU: {cpu_hand} Final Score: {cpu_score}")


play()
while input("Do you want to play again? yes or no: ") == "yes":
    play()
