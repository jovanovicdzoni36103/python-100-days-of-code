import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
    display.append("_")

lives = 6
end_of_game = False

print(" ".join(display))

# game loop
while not end_of_game:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
    #  is, "Wrong" if it's not.
    if guess in chosen_word:
        print("Right")
        # update blanks
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        print("Wrong")
        lives -= 1
        print(f"Lives remaining: {lives}")

    print(" ".join(display))

    # check win
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # check loss
    if lives == 0:
        end_of_game = True
        print(f"You lose! The word was '{chosen_word}'.")

print("GAME OVER")