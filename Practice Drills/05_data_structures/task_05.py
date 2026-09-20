"""
TASK 05 - Filter Dataset by Condition                     [Level 5]

Given:   dataset = [
            {"id": 1, "accuracy": 0.92},
            {"id": 2, "accuracy": 0.65},
            {"id": 3, "accuracy": 0.81},
            {"id": 4, "accuracy": 0.55},
        ]

Create a new list containing only samples with accuracy >= 0.8.
Print only their ID values.

AI/ML: Filtering data by threshold (e.g., keeping only confident predictions)
is something you do all the time, long before reaching for Pandas or NumPy tools.
"""

# Solution:

dataset = [
    {"id": 1, "accuracy": 0.92},
    {"id": 2, "accuracy": 0.65},
    {"id": 3, "accuracy": 0.81},
    {"id": 4, "accuracy": 0.55},
]
filtered_dataset = [sample for sample in dataset if sample["accuracy"] >= 0.8]

for sample in filtered_dataset:
    print(f"Sample ID: {sample['id']}")