"""
TASK 02 - Process only even indices                       [Level 2]

Given:   scores = [0.55, 0.61, 0.72, 0.80, 0.44, 0.90]

Print only the values at even indices (0, 2, 4, ...).

Condition: Use for and range(), do not use slicing.

AI/ML: With large datasets, you sometimes process every N-th row (e.g., for a quick sample check instead of the entire dataset). range() with a step is the way to express this.
"""

# Solution:
scores = [0.55, 0.61, 0.72, 0.80, 0.44, 0.90]

for i in range(0, len(scores), 2):
    print(scores[i])