"""
TASK 01 - Base Class and Subclass                          [Level 3]

Use the base class Model from the previous module (name, accuracy).

Create a subclass ClassifierModel that inherits from Model, with no additional
code (just pass or inherited __init__).

Create a ClassifierModel object and print its name and
accuracy attributes.

AI/ML: Inheritance allows you to have a general Model class, and then specific versions for classifiers, regressors, etc., without repeating code.
"""

class Model:
    def __init__(self, name, accuracy):
        self.name = name
        self.accuracy = accuracy


class ClassifierModel(Model):
    pass


model = ClassifierModel("resnet-50", 0.92)
print(model.name)
print(model.accuracy)