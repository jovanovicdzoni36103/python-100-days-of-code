import random
import string

# ==========================================
# LEVEL 3: Functions + Algorithmic Thinking (Tasks 23–34)
# ==========================================


# TASK 23: Calculator Function
# Create a function calculator(a, b, operation) that takes two numbers and an operator (+, -, *, /) and returns the result.

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Error: Division by zero"
    return "Error: Invalid operation"

print("Task 23 Result:", calculator(10, 5, "/"))


# TASK 24: Factorial Function
# Create a function factorial(n) that calculates the factorial of a given number (n!).

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Task 24 Result:", factorial(5))


# TASK 25: Prime Number Function
# Create a function is_prime(number) that returns True if the number is prime, otherwise False.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Task 25 Result:", is_prime(17))


# TASK 26: Random Password Generator
# Create a function generate_password(length) that returns a random string of a given length.

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

print("Task 26 Result:", generate_password(12))


# TASK 27: Merge Two Dictionaries
# Create a function that takes two dictionaries and merges them into a single new dictionary.

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
print("Task 27 Result:", merge_dictionaries(d1, d2))


# TASK 28: Linear Search
# Create a function linear_search(lst, target) that returns the index of the requested element or -1 if not found.

def linear_search(lst, target):
    for index, item in enumerate(lst):
        if item == target:
            return index
    return -1

print("Task 28 Result:", linear_search([10, 20, 30, 40], 30))


# TASK 29: Remove Duplicates
# Create a function that takes a list and returns a new list without duplicate elements.

def remove_duplicates(lst):
    unique_items = []
    for item in lst:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

print("Task 29 Result:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# TASK 30: Convert Seconds to HH:MM:SS
# Create a function format_time(seconds) that converts total seconds into HH:MM:SS format.

def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print("Task 30 Result:", format_time(3665))


# TASK 31: Fibonacci Sequence
# Create a function fibonacci(n) that generates the first N elements of the Fibonacci sequence.

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print("Task 31 Result:", fibonacci(8))


# TASK 32: Word Censorship
# Create a function censor(text, forbidden_words) that replaces forbidden words with "***".

def censor(text, forbidden_words):
    for word in forbidden_words:
        text = text.replace(word, "***")
    return text

print("Task 32 Result:", censor("Python is bad and slow", ["bad", "slow"]))


# TASK 33: Anagram Check
# Create a function is_anagram(word1, word2) that returns True if the words are anagrams.

def is_anagram(word1, word2):
    w1 = word1.lower().replace(" ", "")
    w2 = word2.lower().replace(" ", "")
    return sorted(w1) == sorted(w2)

print("Task 33 Result:", is_anagram("listen", "silent"))


# TASK 34: Dice Simulation
# Create a function that simulates rolling 2 dice and returns the total sum and whether a double was rolled.

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    is_double = (die1 == die2)
    return total, is_double

total_sum, double_rolled = roll_dice()
print(f"Task 34 Result: Total sum: {total_sum}, Double rolled: {double_rolled}")