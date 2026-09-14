"""
TASK 03 - Split Sample into Train or Test Group         [Level 3]

Given:   sample_index = 17

Rule: If sample_index is divisible by 5 (no remainder), the sample goes into
the "test" group. Otherwise, it goes into the "train" group.

Print which group the sample with the given index belongs to.

Hint: Use `%` (modulo).

AI/ML: Splitting a dataset into train and test sets is one of the first steps
in any ML project. Modulo is a simple way to do this deterministically.
"""

# Solution:
sample_index = 17

if sample_index % 5 == 0:
    group = "test"
else:
    group = "train"

print(f"Sample {sample_index} belongs to the '{group}' group.")