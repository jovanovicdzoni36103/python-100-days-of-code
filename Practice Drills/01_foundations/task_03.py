"""
TASK 03 — Average of Two Models
Level 2 (Slightly harder)

Task: Two models have given their confidence scores. Find their average and
print it rounded to 3 decimal places.

model_a_confidence = 0.812
model_b_confidence = 0.734

Example:
Average ensemble confidence: 0.773

Hint: average = (a + b) / 2, and for rounding use round(number, 3)

(By the way: this is the simplest form of an "ensemble" approach in AI.)
"""

model_a_confidence = 0.812
model_b_confidence = 0.734

average_models_confidence = round((model_a_confidence + model_b_confidence) / 2, 3)
print(f"model_a_confidence: {model_a_confidence}\n"
      f"model_b_confidence: {model_b_confidence}\n"
      f"average_models_confidence: {average_models_confidence}")