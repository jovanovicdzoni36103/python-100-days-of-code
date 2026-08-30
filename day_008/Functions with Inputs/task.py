"""

# PAUSE 1 - Review Solution

def greet():
print("Hello!")
print("How are you today?")
print("Hope you are having a great day!")

greet()

# Function with Inputs Example

def greet_with_name(name):
print(f"Hello {name}!")
print(f"How are you today, {name}?")
print("Hope you are having a great day!")

greet_with_name("Angela")

# Parameters vs Arguments

* Parameter: The variable name defined inside the function parentheses (e.g., 'name' in 'def greet(name):').
* Argument: The actual value passed into the function when it is called (e.g., '"Angela"' in 'greet("Angela")').
"""

"""
CODING EXERCISE

Life in Weeks
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left,
if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.

Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

**Warning** The function must be called life_in_weeks for the tests to pass.
Also the output must have the same punctuation and spelling as the example. Including the full stop!

Example Input
56

Example Output
You have 1768 weeks left.

How to test your code and see your output?

Udemy coding exercises do not have a console, so you cannot use input() .
You will need to call your function with hard-coded values like so:
"""

def life_in_weeks(age):
    if 1 <= age <= 90:
        years_left = 90 - age
        weeks_left = years_left * 52 # Weeks in a year
        print(f"You have {weeks_left} weeks left.")
    else:
        print("Invalid age.")


life_in_weeks(12)