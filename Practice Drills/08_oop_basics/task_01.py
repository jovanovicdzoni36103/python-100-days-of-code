"""
TASK 01 - Model Class                                     [Level 2]

Create a class Model with __init__(self, name, accuracy) that sets
attributes self.name and self.accuracy.

Add a summary() method that returns the string:
Output:  Model 'sentiment-v2' has accuracy 0.87

Create one object and call summary().

AI/ML: The Model class is a way to keep the name, accuracy, and all other properties of a model in one place, instead of a bunch of separate variables.
"""

class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def summary(self):
        return f"Model '{self.name}' has accuracy {self.accuracy}"


model = Model("sentiment-v2", 0.87)
print(model.summary())