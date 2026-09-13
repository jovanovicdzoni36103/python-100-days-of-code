"""
TASK 01 — Print Model Result
Level 1 (Easiest)

Task: Imagine you received a result from an AI model. Create 3
variables - model name, prediction, and confidence (a number) - and print
them in a single sentence using a single f-string.

Example:
Model 'sentiment-v2' says: positive (confidence: 0.91)

Hint: An f-string looks like this - f"text {variable} text"

(By the way: this is how every program displays an AI result to the user.)
"""

model_name = "Claude Opus 4.8"
prediction = "Positive"
confidence = 0.91

print(f"Model '{model_name}' says: {prediction} (confidence: {confidence})")