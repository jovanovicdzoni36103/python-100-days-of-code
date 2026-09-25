"""
TASK 01 - Fix TypeError in Output                      [Level 2]

This code throws an error:

confidence = 0.91
print("Confidence: " + confidence)

Run it, read the error from the terminal, and fix it so that it outputs:
Output:  Confidence: 0.91

Condition: Do not change the value of the confidence variable.

AI/ML: TypeError due to mixing string and float values is one of the most common errors when outputting model results. It is worth recognizing at first glance.
"""

confidence = 0.91
print(f"Confidence: {confidence}")