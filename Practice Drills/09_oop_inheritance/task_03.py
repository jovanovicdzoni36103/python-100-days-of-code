"""
TASK 03 - super().__init__() and a new attribute           [Level 4]

Create a RegressorModel(Model) subclass that, alongside name and accuracy,
has an additional attribute mse (mean squared error).

Condition: Call super().__init__(name, accuracy) to set the inherited
attributes, then add self.mse = mse.

Create an object and print all three attributes.

AI/ML: When a subclass adds its own specific data (e.g., regression has mse, while classification has f1_score), super().__init__() keeps the common part without repetition.
"""

class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy


class RegressorModel(Model):
    def __init__(self, name, accuracy, mse):
        super().__init__(name, accuracy)
        self.mse = mse


model = RegressorModel("house-prices-v1", 0.88, 0.015)
print(model.name)
print(model.accuracy)
print(model.mse)