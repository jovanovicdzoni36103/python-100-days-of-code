"""
TASK 02 - Check If Prediction Is Valid                 [Level 2]

Given:   label = "positive"
        confidence = 0.87

A prediction is valid if:
- confidence is between 0 and 1 (inclusive)
- label is not an empty string

Print "Valid prediction" or "Invalid prediction".

Condition: Use `and` / `or`, without nested `if` statements.

AI/ML: Before saving or displaying a prediction to the user,
you verify whether it makes sense. This is the basic form of model output validation.
"""

# Solution:
label = "positive"
confidence = 0.87

if 0 <= confidence <= 1 and label != "":
    print("Valid prediction")
else:
    print("Invalid prediction")