"""
TASK 01 - List of Active Models                            [Level 1]

Create a list named `models` with three model names of your choice.

Add a new model to the end of the list using .append().
Remove the first model from the list using .remove() or del.

Print the list after each modification.

AI/ML: A list of active models (in production or currently being tested)
is something you frequently maintain and update while working on an ML system.
"""

# Solution:

models = ["ResNet-50", "BERT", "GPT-4o"]
print(f"Initial list of models: {models}")

models.append("Llama-3")
print(f"After adding a model: {models}")
del models[0]
print(f"After removing the first model: {models}")