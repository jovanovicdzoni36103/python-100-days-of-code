"""
TASK 03 - Method That Calculates a Value                 [Level 3]

Add an is_reliable() method to the Model class that returns True if
self.accuracy is greater than 0.75, otherwise False.

Create two objects (one above the threshold, one below) and print the result of
is_reliable() for both.

AI/ML: A method that returns a yes/no decision based on object attributes (e.g., 'is the model good enough for production') is a common pattern in ML code.
"""

class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def is_reliable(self):
        return self.accuracy > 0.75


model_a = Model("bert-base", 0.85)
model_b = Model("baseline-v1", 0.65)

print(model_a.is_reliable())
print(model_b.is_reliable())