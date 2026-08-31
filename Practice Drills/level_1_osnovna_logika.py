# ==========================================
# LEVEL 1: Basic Logic (Tasks 1–10)
# ==========================================

# TASK 1: Message Output and Input
# Ask the user for their name and print the message: "Hello [name], welcome to Python exercises!"

name = input("What is your name?\n")
print(f"Hello {name}, welcome to Python exercises!")


# TASK 2: Age Calculator
# Ask the user for their birth year, calculate how old they will be in the year 2026, and print the result.

birth_year = input("What year were you born?\n")
print(f"The user is {2026 - int(birth_year)} years old")


# TASK 3: Even or Odd Check
# Enter an integer and print whether the number is EVEN or ODD.

number = 5
if number % 2 == 0:
    print("EVEN")
else:
    print("ODD")


# TASK 4: Temperature Converter
# Enter a temperature in Celsius and convert it to Fahrenheit (F = C * 9/5 + 32).

temp_celsius = 25

def temperature_converter():
    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    return temp_fahrenheit

print(temperature_converter())


# TASK 5: Discount Calculator
# Enter the price of an item and the discount percentage, then calculate and print the final price after discount.

price = float(input("Enter the item price: "))
discount_percent = float(input("Enter the discount percentage (%): "))
final_price = price - (price * (discount_percent / 100))
print(f"Final price after discount: {final_price}")


# TASK 6: Comparing Two Numbers
# Enter two numbers and print which one is greater, or print that they are equal if they are the same.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("The numbers are equal")


# TASK 7: BMI Calculator
# Ask the user for their weight (kg) and height (m), calculate BMI (weight / height^2), and print the result.

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi}")


# TASK 8: Sign Check
# Enter a number and print whether it is POSITIVE, NEGATIVE, or ZERO.

num_check = float(input("Enter a number: "))

if num_check > 0:
    print("POSITIVE")
elif num_check < 0:
    print("NEGATIVE")
else:
    print("ZERO")


# TASK 9: F-string Formatting
# Enter first name, last name, and age, then print the sentence: "First Name: [first_name] | Last Name: [last_name] | Age: [age]".

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
user_age = input("Enter age: ")

print(f"First Name: {first_name} | Last Name: {last_name} | Age: {user_age}")


# TASK 10: Leap Year Check
# Enter a year and check if it is a leap year (a year is a leap year if it is divisible by 4).

year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")