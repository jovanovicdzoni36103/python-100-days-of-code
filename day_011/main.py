import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Sve funkcije su ovde
def deal_card():
    card = random.choice(cards)
    return card


def sum_score(hand):
    total = sum(hand)

    while total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return total

def compare_scores(user_hand, bot_hand):
    user_score = sum_score(user_hand)
    bot_score = sum_score(bot_hand)

    user_has_bj = user_score == 21 and len(user_hand) == 2
    bot_has_bj = bot_score == 21 and len(bot_hand) == 2

    if user_has_bj and bot_has_bj:
        return "Draw! Both players have Blackjack."
    elif user_has_bj:
        return "You have Blackjack (21 from two cards)!"
    elif bot_has_bj:
        return "Loss! Computer has Blackjack."
    elif user_score > 21:
        return "Player BUSTED! Computer wins."
    elif bot_score > 21:
        return "Computer BUSTED! Player wins."
    elif user_score == bot_score:
        return "Draw!"
    elif user_score > bot_score:
        return "Player wins!"
    else:
        return "Computer wins!"

user_hand = []
while len(user_hand) < 2:
    user_hand.append(deal_card())
print(f"User cards in hand: {user_hand}, sum of hand: {sum_score(user_hand)}")

bot_hand = []
while len(bot_hand) < 2:
    bot_hand.append(deal_card())
print(f"One cards in hand: {bot_hand[0]}")

user_hit_choice = input("Do you want one more card? y/n: ")

while user_hit_choice == "y":
    user_hand.append(deal_card())

    current_score = sum_score(user_hand)
    print(f"User cards: {user_hand}, current sum: {current_score}")

    if current_score > 21:
        print("You went over 21.")
        break

    user_hit_choice = input("Do you want one more card? y/n: ")

bot_score = sum_score(bot_hand)

while bot_score < 17:
    bot_hand.append(deal_card())
    bot_score = sum_score(bot_hand)

print(f"Bot final cards: {bot_hand}, final sum: {bot_score}")
print(f"\nUser final cards: {user_hand}, final sum: {sum_score(user_hand)}")

result = compare_scores(user_hand, bot_hand)
print(f"\nREZULTAT: {result}")