"""
TASK 04 - Dataset Class with a List of Samples           [Level 4]

Create a class Dataset with __init__(self) that sets
self.samples = [] (an empty list).

Add an add_sample(value) method that adds a value to self.samples.
Add an average() method that returns the average of all samples in self.samples.

Create an object, add 4 values, print average().

AI/ML: A class that stores data and has methods for adding and calculating over it is a simplified version of what DataLoader classes do in real ML libraries.
"""

class Dataset:
    def __init__(self):
        self.samples = []

    def add_sample(self, value):
        self.samples.append(value)

    def average(self):
        if not self.samples:
            return 0
        return sum(self.samples) / len(self.samples)


dataset = Dataset()
dataset.add_sample(0.8)
dataset.add_sample(0.9)
dataset.add_sample(0.7)
dataset.add_sample(0.85)

print(dataset.average())