from art import logo
from game_data import data
import random
print(logo)
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (
        f"Account name: {account_name}\n"
        f"Account description: {account_description}\n"
        f"from: {account_country}"
    )
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"compare a:\n{format_data(account_a)}\n")
    print(f"against b:\n{format_data(account_b)}\n")
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    guess = input("who has more followers type 'a' or 'b' ").lower()
    is_correct = check_answer(guess, a_followers, b_followers)
    if is_correct:
        score += 1
        print(f"tacno trenutni skor ti je {score}")
    else:
        game_should_continue = False
        print(f"nazalost pogresio si tvoj konacni skor je {score}")
