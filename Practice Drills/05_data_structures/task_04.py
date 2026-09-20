"""
TASK 04 - Nested Dictionary: Metrics of Multiple Models   [Level 4]

Create a dictionary `results` where each key is a model name, and the value is a dictionary
containing "accuracy" and "f1_score".

Example structure:
results = {
    "model_a": {"accuracy": 0.81, "f1_score": 0.79},
    "model_b": {"accuracy": 0.88, "f1_score": 0.85},
}

Print the name of the model with the highest `accuracy` value.

AI/ML: When comparing multiple experiments, results are naturally organized
as a dictionary of dictionaries: model -> its metrics. This forms the foundation
for later comparison in Pandas.
"""

# Solution:
results = {
    "model_a": {"accuracy": 0.81, "f1_score": 0.79},
    "model_b": {"accuracy": 0.88, "f1_score": 0.85},
    "model_c": {"accuracy": 0.84, "f1_score": 0.82}
}

best_model = None
highest_accuracy = -1.0

for model_name, metrics in results.items():
    if metrics["accuracy"] > highest_accuracy:
        highest_accuracy = metrics["accuracy"]
        best_model = model_name

print(f"Model with the highest accuracy: {best_model} ({highest_accuracy})")