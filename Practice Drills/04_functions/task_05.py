"""
TASK 05 - Complete the function and write a docstring              [Level 5]

Given the starting function:

def weighted_average(scores, weights):
    ...

Task:
- Complete the function body: multiply each score by its corresponding weight,
  sum them up, and divide by the sum of weights.
- Write a one-sentence docstring explaining what the function does.

Given: scores = [0.8, 0.6, 0.9]
        weights = [0.5, 0.2, 0.3]

AI/ML: Weighted average is the foundation of ensembling: combining multiple models, not with equal impact, but according to how much confidence you have in each.
"""

scores = [0.8, 0.6, 0.9]
weights = [0.5, 0.2, 0.3]


def weighted_average(scores, weights):
    """Izračunava ponderisani prosečni skor na osnovu zadatih vrednosti i odgovarajućih težina."""
    total_weighted_sum = 0

    for score, weight in zip(scores, weights):
        total_weighted_sum += score * weight

    total_weights = sum(weights)

    return total_weighted_sum / total_weights


result = weighted_average(scores, weights)
print(f"Weighted average: {result}")