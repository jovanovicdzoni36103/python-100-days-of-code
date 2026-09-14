"""
TASK 01 - Print all accuracy values                   [Level 1]

Given:   accuracies = [0.81, 0.76, 0.93, 0.68]

Iterate through the list and print each value with a sequence number, starting from 1.

Output:
Model 1: 0.81
Model 2: 0.76
Model 3: 0.93
Model 4: 0.68

AI/ML: Model results almost never arrive individually, but rather as a list. A for loop is the fundamental way to inspect and print them.
"""

# Solution:
accuracies = [0.81, 0.76, 0.93, 0.68]

for i, acc in enumerate(accuracies, 1):
    print(f"Model {i}: {acc}")