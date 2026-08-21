# day_003


# Task 1
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")


"""
Day 3 - Lesson 26: Pizza Order Practice (Python Pizza Deliveries)
Course: 100 Days of Code™: The Complete Python Pro Bootcamp

Instructions:
Build an automatic pizza order program that calculates the final bill
based on a customer's choice of size and extra toppings.

Rules and Pricing:
1. Pizza Size (size):
   - Small Pizza (S): $15
   - Medium Pizza (M): $20
   - Large Pizza (L): $25

2. Pepperoni Topping (add_pepperoni):
   - Pepperoni for Small Pizza (S): +$2
   - Pepperoni for Medium (M) or Large Pizza (L): +$3

3. Extra Cheese (extra_cheese):
   - Extra cheese for any size: +$1

Example 1:
   Input: size = "L", add_pepperoni = "Y", extra_cheese = "N"
   Output: Your final bill is: $28.

Example 2:
   Input: size = "S", add_pepperoni = "Y", extra_cheese = "Y"
   Output: Your final bill is: $18.
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0

if size == "S": bill += 15
elif size == "M": bill += 20
elif size == "L": bill += 25

if add_pepperoni == "Y":
    if size == "S": bill += 2
    else: bill += 3

if extra_cheese == "Y": bill += 1
else: bill += 0

print(f"Your final bill is: {bill}")


"""
Day 3 Project: Treasure Island
Build a text based adventure game that follows this flowchart.

Start:
    Print: "Welcome to Treasure Island."
           "Your mission is to find the treasure."

Step 1 - Crossroad:
    Ask: "left or right?"
        "left"                  -> continue to Step 2
        "right" or anything else -> "Fall into a hole. Game Over."

Step 2 - Lake:
    Ask: "swim or wait?"
        "wait"                  -> continue to Step 3
        "swim" or anything else -> "Attacked by trout. Game Over."

Step 3 - Three doors:
    Ask: "Which door? red, blue or yellow?"
        "red"           -> "Burned by fire. Game Over."
        "blue"          -> "Eaten by beasts. Game Over."
        "yellow"        -> "You Win!"
        anything else   -> "Game Over."
"""

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("left or right? ")

if choice == "left":
    choice = input("swim or wait? ")

    if choice == "wait":
        choice = input("Which door? red, blue or yellow? ")

        if choice == "red":
            print("Burned by fire. Game Over.")
        elif choice == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice == "yellow":
            print("You Win!")
        else:
            print("Game Over.")

    elif choice == "swim":
        print("Attacked by trout. Game Over.")
    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over.")