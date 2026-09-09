# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# # Functions with more than 1 input
# def greet_with(name, location):
#     print(f"My name is {name} and I live in {location}")
#
# greet_with("Nikola", "Belgrade")
# greet_with(location="London", name="Anglela")

"""
Love Calculator
💪 This is a difficult challenge! 💪

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 

Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 

Total = 3 

Love Score = 53

Example Input 
calculate_love_score("Kanye West", "Kim Kardashian")

Example Output
42
"""

def calculate_love_score(name1, name2):
    names = (name1 + name2).lower()

    t = names.count("t")
    r = names.count("r")
    u = names.count("u")
    e = names.count("e")
    total_true = t + r + u + e

    l = names.count("l")
    o = names.count("o")
    v = names.count("v")
    e_love = names.count("e")
    total_love = l + o + v + e_love

    love_score = str(total_true) + str(total_love)
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")