"""
TASK 05 - Compare every pair of models                     [Level 4]

Given:   models = {"A": 0.81, "B": 0.77, "C": 0.90}

For each pair of distinct models, print which one is better.

Output (order does not matter):
A vs B: A is better
A vs C: C is better
B vs C: C is better

Hint: nested for loop over .items().

AI/ML: Comparing multiple models against each other (not just against a single threshold) is a common step when choosing which model goes to production.
"""

# Solution:
models = {"A": 0.81, "B": 0.77, "C": 0.90}
items = list(models.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        name1, score1 = items[i]
        name2, score2 = items[j]

        better = name1 if score1 > score2 else name2
        print(f"{name1} vs {name2}: {better} is better")