"""
PROJECT: U.S. States Game (Pandas & Turtle)

GOAL:
Build an interactive map quiz game where the user guesses all 50 U.S. states.
When a user types a correct state name, the text appears on the map at its
exact coordinates. The game keeps track of the score and exports missed states
to a CSV file upon exit.

PREREQUISITES:
1. Python installed with `pandas` and `turtle` (built-in).
2. A CSV file named `50_states.csv` with columns: `state`, `x`, `y`.
3. An image file named `blank_states_img.gif` in the project directory.

REQUIREMENTS & LOGIC:
1. Screen Setup:
   - Create a turtle screen with title "U.S. States Game".
   - Set `blank_states_img.gif` as the screen background shape.

2. Data Handling (Pandas):
   - Load `50_states.csv` into a DataFrame.
   - Extract the `state` column into a Python list (`all_states`).
   - Maintain a `guessed_states` list to keep track of correct entries.

3. Game Loop:
   - Prompt the user using `screen.textinput()` showing current score (e.g., "12/50").
   - Convert user input to Title Case (e.g., "texas" -> "Texas").
   - If user inputs "Exit":
     * Filter remaining un-guessed states.
     * Export missed states to `states_to_learn.csv`.
     * Break the loop and close.
   - If input matches a state in `all_states` and hasn't been guessed yet:
     * Add state to `guessed_states`.
     * Extract x and y coordinates for that specific state.
     * Use a hidden Turtle to write the state name at (x, y).

4. Win Condition:
   - When `len(guessed_states) == 50`, the player wins and the game ends.
"""

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        break

    answer_state = answer_state.strip().title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df_missing = pd.DataFrame(missing_states, columns=["state"])
        df_missing.to_csv("states_to_learn.csv", index=False)
        print("Progress saved to 'states_to_learn.csv'. Goodbye!")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_data = data[data.state == answer_state]

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        x_coord = int(state_data.x.iloc[0])
        y_coord = int(state_data.y.iloc[0])

        writer.goto(x_coord, y_coord)
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

screen.mainloop()