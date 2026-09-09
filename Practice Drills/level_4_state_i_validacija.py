import random

# ==========================================
# LEVEL 4: State, Validation & Complex Problems (Tasks 35–48)
# ==========================================


# TASK 35: Email Address Validation
# Check if an entered email address contains "@" and a "." after the "@" symbol.

def validate_email(email):
    if "@" in email:
        at_index = email.find("@")
        if "." in email[at_index + 1:]:
            return True
    return False

print("Task 35 Result:", validate_email("user@example.com"))


# TASK 36: Login System with Attempt Limit
# Implement a login system with 3 allowed attempts. Lock the account after 3 failed attempts.

correct_password = "secret123"
attempts = 3
user_input = "secret123"  # Simulated user input

while attempts > 0:
    if user_input == correct_password:
        print("Task 36 Result: Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. Attempts remaining: {attempts}")

if attempts == 0:
    print("Task 36 Result: Account locked due to 3 failed attempts.")


# TASK 37: Student Database Management
# Use a dictionary where keys are student names and values are their grades. Allow adding and updating grades.

student_db = {"Alice": 5, "Bob": 4}

def update_student(db, name, grade):
    db[name] = grade
    return db

update_student(student_db, "Charlie", 5)
update_student(student_db, "Alice", 4)
print("Task 37 Result:", student_db)


# TASK 38: Shopping Cart System
# Create a system where items with prices are added to a cart, calculating the total price at the end.

cart = []

def add_to_cart(cart_list, item_name, price):
    cart_list.append({"item": item_name, "price": price})

add_to_cart(cart, "Laptop", 800)
add_to_cart(cart, "Mouse", 25)

total_price = sum(item["price"] for item in cart)
print(f"Task 38 Result: Cart: {cart}, Total: ${total_price}")


# TASK 39: Rock, Paper, Scissors with Score Tracking
# Create a game tracking scores (Player vs. Computer) until one reaches 3 wins.

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player_choice = "rock"  # Simulated player move
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        continue
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        player_score += 1
    else:
        computer_score += 1

print(f"Task 39 Result: Final Score - Player: {player_score}, Computer: {computer_score}")


# TASK 40: ATM Simulation
# Create an ATM menu: 1. Check Balance, 2. Deposit, 3. Withdraw (checking for sufficient funds).

balance = 1000.0

def atm(action, amount=0.0):
    global balance
    if action == "check":
        return f"Current balance: ${balance:.2f}"
    elif action == "deposit":
        balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${balance:.2f}"
    elif action == "withdraw":
        if amount <= balance:
            balance -= amount
            return f"Withdrew ${amount:.2f}. Remaining balance: ${balance:.2f}"
        return "Transaction failed: Insufficient funds."

print("Task 40 Result:", atm("check"))
print("Task 40 Result:", atm("deposit", 200))
print("Task 40 Result:", atm("withdraw", 500))


# TASK 41: Text Cleaning and Formatting
# Input text with multiple consecutive spaces and inconsistent casing, clean it, and format properly.

raw_text = "   python   iS   aWesome   aNd   pOWerfUL   "
words = raw_text.split()
cleaned_text = " ".join(words).capitalize()

print("Task 41 Result:", f"'{cleaned_text}'")


# TASK 42: ID / Phone Number Validation
# Check if an entered string consists solely of digits and has exactly 13 digits (for JMBG) or 10 digits.

def validate_id_or_phone(number_str):
    if number_str.isdigit():
        length = len(number_str)
        if length == 13:
            return "Valid JMBG (13 digits)"
        elif length == 10:
            return "Valid Phone Number (10 digits)"
    return "Invalid input"

print("Task 42 Result:", validate_id_or_phone("0101990710015"))
print("Task 42 Result:", validate_id_or_phone("0641234567"))


# TASK 43: Character Frequency in Text
# Create a dictionary counting how many times each character appears in an entered text.

text_input = "hello world"
char_frequency = {}

for char in text_input:
    if char != " ":
        char_frequency[char] = char_frequency.get(char, 0) + 1

print("Task 43 Result:", char_frequency)


# TASK 44: Roman Numerals to Arabic
# Create a function that converts Roman numerals (I, V, X, L, C, D, M) to Arabic numbers.

def roman_to_int(roman_str):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(roman_str.upper()):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

print("Task 44 Result (MCMXCIV):", roman_to_int("MCMXCIV"))


# TASK 45: Savings Simulation
# Calculate savings growth over N years with a specified annual interest rate.

def calculate_savings(principal, rate, years):
    total = principal
    for _ in range(years):
        total += total * (rate / 100)
    return total

print("Task 45 Result:", f"${calculate_savings(1000, 5, 10):.2f}")


# TASK 46: Traffic Light System (State Transition)
# Simulate traffic light state transitions: Red -> Yellow -> Green -> Yellow -> Red.

traffic_cycle = ["Red", "Yellow", "Green", "Yellow", "Red"]

print("Task 46 Result:")
for state in traffic_cycle:
    print(f"Signal: {state}")


# TASK 47: Form Validation with Error Handling (try-except)
# Input age and price, handling ValueError exceptions if non-numeric values are entered.

def validate_form(age_str, price_str):
    try:
        age = int(age_str)
        price = float(price_str)
        if age < 0 or price < 0:
            return "Error: Values must be non-negative."
        return f"Valid input: Age={age}, Price=${price:.2f}"
    except ValueError:
        return "Error: Please enter valid numeric values."

print("Task 47 Result (Success):", validate_form("25", "99.99"))
print("Task 47 Result (Error):", validate_form("twenty", "99.99"))


# TASK 48: Sorting List of Dictionaries
# Sort a list of items [{'name': 'A', 'price': 100}, {'name': 'B', 'price': 50}] by price ascending.

items = [
    {"name": "Laptop", "price": 800},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75}
]

sorted_items = sorted(items, key=lambda item: item["price"])
print("Task 48 Result:", sorted_items)