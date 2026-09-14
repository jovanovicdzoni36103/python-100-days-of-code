"""
TASK 04 - Simulate a Random Prediction                  [Level 4]

Create a list of labels: ["positive", "neutral", "negative"].

Randomly select one label and a random confidence between 0.5 and 1.0
(rounded to 2 decimal places).

Print the output in the format:
Output:  Predicted: negative (confidence: 0.73)

Condition: Use `random.choice()` and `random.uniform()`.

AI/ML: The random module is used to simulate models before a real model exists,
and for data augmentation (shuffling, random sampling).
"""

# Solution:
import random

labels = ["positive", "neutral", "negative"]

selected_label = random.choice(labels)
confidence = random.uniform(0.5, 1.0)

print(f"Predicted: {selected_label} (confidence: {confidence:.2f})")