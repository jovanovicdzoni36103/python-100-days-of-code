"""
TASK 04 - Print-debug: incorrect number of filtered samples  [Level 4]

This code should keep only samples with accuracy > 0.7, but it returns
the wrong number of samples:

samples = [0.65, 0.72, 0.81, 0.55, 0.90, 0.68]
kept = []
for s in samples:
    if s > 0.7:
        kept.append(s)
    kept.append(s)

print(f"Kept: {len(kept)} of {len(samples)}")

Add print() lines to see what is happening inside the loop, find
the error and fix it.

AI/ML: Incorrect indentation or wrong location of a line in a filtering loop is a common reason why a dataset has more rows than expected after 'cleaning'.
"""

samples = [0.65, 0.72, 0.81, 0.55, 0.90, 0.68]
kept = []
for s in samples:
    if s > 0.7:
        kept.append(s)

print(f"Kept: {len(kept)} of {len(samples)}")