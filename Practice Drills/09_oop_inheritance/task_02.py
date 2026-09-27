"""
TASK 02 - Method Override in Subclass                      [Level 4]

The ClassifierModel subclass should have its own version of the summary() method
that returns:
Output:  Classifier 'spam-detector' - accuracy 0.91

Condition: The base class Model retains its original summary() method;
only the subclass overrides it.

AI/ML: Different types of models (classifier, regressor) have different relevant metrics, so they need different result outputs. Overriding is a way to express that.
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


model = ClassifierModel("spam-detector", 0.91)
print(model.summary())