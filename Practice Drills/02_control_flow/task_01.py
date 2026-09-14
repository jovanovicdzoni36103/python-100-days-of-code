"""
TASK 01 - Classify Prediction by Threshold              [Level 1]

Given:   confidence = 0.42

If confidence >= 0.7 -> "high"
If confidence >= 0.4 -> "medium"
Otherwise -> "low"

Print the result.

Output:  Confidence level: medium

AI/ML: Models almost always return a number (confidence), not a word.
if/elif/else is what converts that number into a human-readable category.
"""

# Solution:
confidence = 0.42

if confidence >= 0.7:
    level = "high"
elif confidence >= 0.4:
    level = "medium"
else:
    level = "low"

print(f"Confidence level: {level}")