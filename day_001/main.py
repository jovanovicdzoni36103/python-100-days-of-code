# day_001
# Tema: Osnovne komande


# 1
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")


# 2
# Fix the code below 👇

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")


# 3
# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice.
# Write 3 lines of code to switch the contents of the variables.
# You are not allowed to type the words "milk" or "juice".
# You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"
glass3 = ""

glass3 = glass1
glass1 = glass2
glass2= glass3

print("This is glass 1 - " + glass1)
print("This is glass 2 - " + glass2)


# 3
# Create a greetings for your program
# Ask the user for the city that they grew up in and store it in variable
# Combine the name of their city and pet and show them their band name

print("Hey! Now I will recommend to you a band name")

city = input("What city did you grow up?")
pet = input("What is your pets name?")

print("Your band name is " + city + " " + pet)