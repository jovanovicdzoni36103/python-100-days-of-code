"""
TASK 03 - Find why the average is wrong                [Level 3]

This code does not throw an error, but gives a wrong result:

scores = [0.8, 0.6, 0.9, 0.7]
total = 0
for s in scores:
    total += s
average = total / 3

print(f"Average: {average}")

Find the error and fix it so that average is the exact average.

AI/ML: Errors that do not throw an exception, but simply give a wrong number (like a wrong denominator here), are more dangerous than actual errors because they easily go unnoticed in model evaluation.
"""

scores = [0.8, 0.6, 0.9, 0.7]
total = 0
for s in scores:
    total += s
average = total / len(scores)

print(f"Average: {average}")