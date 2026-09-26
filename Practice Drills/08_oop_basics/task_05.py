"""
TASK 05 - One Class as an Attribute of Another            [Level 5]

Using the Model class, create an Experiment class with
__init__(self, name, model) that stores self.name and self.model.

Add a report() method that returns the string:
Output:  Experiment 'exp-01' used model 'sentiment-v2' (accuracy: 0.87)

Create a Model object, then an Experiment object that uses it, and call
report().

AI/ML: An experiment in ML is always more than just the model: it has a name, date, configuration. Composition (a class inside a class) is a way to represent that in code.
"""

class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy


class Experiment:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def report(self):
        return f"Experiment '{self.name}' used model '{self.model.name}' (accuracy: {self.model.accuracy})"


model = Model("sentiment-v2", 0.87)
experiment = Experiment("exp-01", model)
print(experiment.report())