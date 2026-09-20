"""
TASK 02 - Dictionary with Metrics for a Single Model      [Level 2]

Create a `metrics` dictionary with keys "accuracy", "precision", "recall"
and values of your choice (floats between 0 and 1).

Print each metric in the format:
Output:  accuracy: 0.87

Condition: Use .items() in a loop, not manual key listing.

AI/ML: Model evaluation results are almost always represented as a dictionary:
{metric: value}. This is the standard format returned by scikit-learn and most ML libraries.
"""

# Solution:

metrics = {
    "accuracy": 0.87,
    "precision": 0.82,
    "recall": 0.91
}

for metric, value in metrics.items():
    print(f"{metric}: {value}")