"""
TASK 03 - Count correct predictions                        [Level 2]

Given:   predicted = ["cat", "dog", "cat", "bird", "dog"]
         actual    = ["cat", "cat", "cat", "bird", "fish"]

Count how many predictions match the actual value at the same index.

Output:  Correct: 3 / 5

AI/ML: This is a manual version of what accuracy_score does in scikit-learn. It is worth knowing how it is calculated before using a built-in function.
"""

# Solution:
predicted = ["cat", "dog", "cat", "bird", "dog"]
actual    = ["cat", "cat", "cat", "bird", "fish"]

correct = 0
for pred, act in zip(predicted, actual):
    if pred == act:
        correct += 1

print(f"Correct: {correct} / {len(predicted)}")