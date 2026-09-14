"""
TASK 04 - Simulate training until accuracy exceeds threshold [Level 3]

Given:   accuracy = 0.5
         target = 0.9

In each iteration, accuracy increases by 0.05. Print accuracy after each
iteration until it reaches or exceeds the target. At the end, print the number of iterations.

Condition: Use a while loop.

AI/ML: Model training is essentially a while loop: 'repeat until the metric improves enough or until the maximum number of epochs passes'.
"""

# Solution:
accuracy = 0.5
target = 0.9
iterations = 0

while accuracy < target:
    accuracy += 0.05
    iterations += 1
    print(f"Iteration {iterations}: {round(accuracy, 2)}")

print(f"Total iterations: {iterations}")