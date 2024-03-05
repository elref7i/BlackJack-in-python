import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Random two cards for each user and computer"""
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user,computer):
    if user == computer:
        return "Draw"
    elif computer == 0:
        return "Lose , opponent a Blackjack"
    elif user == 0:
        return "You Win Blackjack"
    elif user > 21:
        return "You lose Blackjack"
    elif computer > 21:
        return "You Win "
    elif user > computer:
        return "You Win"
    else:
        return "you Lose"


user_card = []
computer_card = []
for i in range(2):
    # random 2 card range
    user_card.append(deal_card())
    computer_card.append(deal_card())

# sum card for each user and computer

game_over = False
while not game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"User card {user_card} = {user_score}")
    print(f"computer card {computer_card[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        ask_user = input("they want to draw another card").lower()
        if ask_user == "yes":
            user_card.append(deal_card())
        else:
            game_over = True


while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)

print(f"computer score {computer_card} the score = {computer_score}")
End = compare_score(user_score,computer_score)
print(End)
