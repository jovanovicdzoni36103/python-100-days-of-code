# day_002

"""
BMI Calculator

The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight.
This is the formula used to calculate it:

bmi is equal to the person's weight divided by the person's height squared.
"""

height = 1.65
weight = 84

bmi = weight / (height ** 2)

print(bmi)


"""
Tip Calculator Project

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:
(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60
"""

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_bill = bill * (1 + tip_percent)
amount_per_person = total_bill / people
final_amount = f"{amount_per_person:.2f}"

print(f"Each person should pay: ${final_amount}")