"""
TASK 01 - Create a function calculate_accuracy()           [Level 1]

Create a function calculate_accuracy(correct, total) that returns
accuracy as a float, rounded to 3 decimal places.

Call it with correct=42, total=50 and print the result.

Output: Accuracy: 0.84

Requirement: The function must use return, not print inside itself.

AI/ML: This is a function you will practically rewrite (or import from a library) in every ML project. The difference between return and print is crucial here: return passes the value further for processing.
"""

def calculate_accuracy(correct, total):
    accuracy = correct / total
    return round(accuracy, 3)

result = calculate_accuracy(42, 50)
print(f"Accuracy: {result}")