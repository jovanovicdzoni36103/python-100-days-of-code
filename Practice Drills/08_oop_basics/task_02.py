"""
TASK 02 - Multiple Instances of the Same Class             [Level 3]

Using the Model class from the previous task, create a list of 3
Model objects with different names and accuracy values.

Iterate through the list and print summary() for each model.

AI/ML: In a real project, you rarely have just one model. A list of objects allows you to apply the same code (summary, comparison) to all models at once.
"""

class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def summary(self):
        return f"Model '{self.name}' has accuracy {self.accuracy}"


models = [
    Model("sentiment-v1", 0.82),
    Model("sentiment-v2", 0.87),
    Model("bert-base", 0.91)
]

for model in models:
    print(model.summary())