"""
TASK 04 - Same Method, Different Models                   [Level 5]

Create a list containing both ClassifierModel and RegressorModel objects
(one or more of each).

Iterate through the list and call summary() on each object in the same loop,
without type checking (if isinstance...).

Print all results.

AI/ML: This is polymorphism: code processing a 'list of models' does not need to know each model's specific type, it just calls the same method. This is how real ML frameworks work.
"""

class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy

    def summary(self):
        return f"Model '{self.name}' has accuracy {self.accuracy}"


class ClassifierModel(Model):
    def summary(self):
        return f"Classifier '{self.name}' - accuracy {self.accuracy}"


class RegressorModel(Model):
    def __init__(self, name, accuracy, mse):
        super().__init__(name, accuracy)
        self.mse = mse

    def summary(self):
        return f"Regressor '{self.name}' - accuracy {self.accuracy} (MSE: {self.mse})"


models = [
    ClassifierModel("spam-detector", 0.91),
    RegressorModel("house-prices-v1", 0.88, 0.015),
    ClassifierModel("sentiment-v2", 0.87)
]

for model in models:
    print(model.summary())