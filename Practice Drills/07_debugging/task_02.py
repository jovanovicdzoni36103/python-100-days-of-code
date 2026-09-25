"""
TASK 02 - Fix IndexError in Loop                      [Level 2]

This code throws an error:

scores = [0.5, 0.7, 0.9]
for i in range(len(scores) + 1):
    print(scores[i])

Run it, read the traceback, find the exact line where the problem is and
fix it.

AI/ML: IndexError due to a loop going one step too far (off-by-one) is a common bug when processing a list of predictions or dataset rows.
"""

scores = [0.5, 0.7, 0.9]
for i in range(len(scores)):
    print(scores[i])