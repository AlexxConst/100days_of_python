import art
import random


def deal_card():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "You lose! Opponent has a Blackjack."
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, current score: {user_score}")
        print(f"Computer's card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand is {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_game()







# def play_blackjack():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     user_hand = random.sample(cards, 2)
#     computer_hand = random.sample(cards, 2)
#
#     user_score = sum(user_hand)
#     computer_score = sum(computer_hand)
#
#     print(f"Your cards: {user_hand}, current score: {user_score}")
#     print(f"Computer's first card: {computer_hand[0]}")
#
#     if 11 in computer_hand and 10 in computer_hand and len(computer_hand) == 2:
#         print(f"Computer has Blackjack! {computer_hand} You lose!😟")
#         return
#
#     if 11 in user_hand and 10 in user_hand and len(user_hand) == 2:
#             print("Blackjack! You win!🎉")
#             return
#
#
#     while True:
#         if user_score > 21:
#             if 11 in user_hand:
#                 user_hand[user_hand.index(11)] = 1
#                 user_score = sum(user_hand)
#             else:
#                 print(f"Your cards: {user_hand}, current score: {user_score}")
#                 print("You went over 21! You lose! 😐")
#                 return
#
#         if user_score == 21:
#             print("Blackjack! You win! 🎉")
#             return
#
#         another_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         if another_card == 'y':
#             # Добавляем новую карту в руку пользователя
#             new_card = random.choice(cards)
#             user_hand.append(new_card)
#             user_score = sum(user_hand)
#         elif another_card == 'n':
#             while computer_score < 17:
#                 computer_hand.append(random.choice(cards))
#                 computer_score = sum(computer_hand)
#
#         print(f"Your final hand: {user_hand}, final score: {user_score}")
#         print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
#
#         # Сравнение очков
#         if computer_score > 21:
#             print("Computer went over 21! You win! 😀")
#         elif user_score > computer_score:
#             print("You win! 😀")
#         elif user_score == computer_score:
#             print("It's draw! 😐")
#         else:
#             print("You lose! 🙁")
#         return
#
# def start_game():
#     while True:
#         start_request = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#         if start_request == 'y':
#             print(art.logo)
#             play_blackjack()
#             # print("\n" * 20)
#         elif start_request == 'n':
#             print("Maybe next time!")
#             break
#         else:
#             print("Invalid input! Please type 'y' or 'n'.")
#
#
# start_game()
