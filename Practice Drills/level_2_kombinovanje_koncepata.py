import random

# ==========================================
# LEVEL 2: Combining Concepts (Tasks 11–22)
# ==========================================


# TASK 11: Sum of numbers from 1 to N
# Enter a number N and calculate the sum of all numbers from 1 to N using a for loop.

n = int(input("Enter a number N: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"The sum of all numbers from 1 to {n} is: {total_sum}")


# TASK 12: Multiplication Table
# Enter a number and print its multiplication table from 1 to 10.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# TASK 13: Count Vowels
# Enter a sentence and calculate how many vowels (a, e, i, o, u) it contains.

sentence = input("Enter a sentence: ").lower()
vowel_count = 0
vowels = ("a", "e", "i", "o", "u")

for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"The sentence contains {vowel_count} vowels.")


# TASK 14: Reverse String
# Enter a word or sentence and print it in reverse.

text = input("Enter text: ")
reversed_text = text[::-1]
print(reversed_text)


# TASK 15: Maximum in List without max()
# Create a list of numbers [12, 45, 2, 89, 34] and find the largest number using a loop without max().

numbers = [12, 45, 2, 89, 34]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print(f"The largest number in the list is: {max_number}")


# TASK 16: Filter Even Numbers
# From a given list of numbers, extract all even numbers into a new list and print it.

all_numbers = [12, 45, 2, 89, 34]
even_numbers = []

for num in all_numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Even numbers: {even_numbers}")


# TASK 17: Number Guessing Game
# Generate a random number from 1 to 10. The user guesses via a while loop until guessed correctly.

target_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != target_number:
    guess = int(input("Incorrect, try again: "))

print("Congratulations! You guessed it!")


# TASK 18: Palindrome Check
# Enter a word and check if it is a palindrome (reads the same forwards and backwards).

word = input("Enter a word: ").lower()

if word == word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")


# TASK 19: Count Words
# Enter a sentence and count how many words it contains.

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)

print(f"The sentence contains {word_count} words.")


# TASK 20: List of Square Numbers
# Generate a list containing squares of numbers from 1 to 15 using list comprehension.

squares = [x ** 2 for x in range(1, 16)]
print(f"Squares from 1 to 15: {squares}")


# TASK 21: Password Strength Validation
# Enter a password and check if it has at least 8 characters.

password = input("Enter a password: ")

if len(password) >= 8:
    print("Password status: Valid (8+ characters)")
else:
    print("Password status: Invalid (Must be at least 8 characters)")


# TASK 22: Average Grade
# Given a list of grades (e.g., [5, 4, 3, 5, 2]), calculate the average grade.

grades = [5, 4, 3, 5, 2]
average_grade = sum(grades) / len(grades)

print(f"The average grade is: {average_grade:.2f}")