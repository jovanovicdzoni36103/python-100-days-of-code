import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("choose difficulty easy or hard ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_number(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"you got it the secret number was {answer}")
        return turns


def guess_number():
    print("welcome to guess my number")
    print("im thinking of a number between 1 and 100")

    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer and turns > 0:
        print(f"you have {turns} attempts remaining")
        guess = int(input("guess a number "))

        turns = check_number(guess, answer, turns)

        if turns == 0:
            print(f"you lost the number was {answer}")


guess_number()