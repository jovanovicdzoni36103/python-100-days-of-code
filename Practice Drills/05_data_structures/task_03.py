"""
TASK 03 - Dataset as a List of Samples                    [Level 3]

Create a list named `dataset` containing 3 samples. Each sample is a dictionary
with the keys "id" and "label", e.g., {"id": 1, "label": "spam"}.

Iterate through `dataset` and print only the `id` of those samples whose `label`
is equal to "spam".

AI/ML: In Python, before a dataset becomes a DataFrame or a NumPy array,
it almost always starts as a list of dictionaries—one dictionary per row of data.
"""

# Solution:

dataset = [
    {"id": 1, "label": "spam"},
    {"id": 2, "label": "ham"},
    {"id": 3, "label": "spam"}
]

for sample in dataset:
    if sample["label"] == "spam":
        print(f"Spam sample ID: {sample['id']}")