"""
TASK 04 - Function returning multiple values              [Level 4]

Given: scores = [0.55, 0.91, 0.63, 0.78, 0.40]

Create a function get_min_max(scores) that returns (min, max) as a tuple,
without using built-in min() and max() functions.

Print: Min: 0.4, Max: 0.91

AI/ML: Model evaluation functions often return multiple values at once (e.g. precision and recall together). Tuple is the simplest way to do that.
"""

scores = [0.55, 0.91, 0.63, 0.78, 0.40]


def get_min_max(scores):
    min_val = scores[0]
    max_val = scores[0]

    for score in scores:
        if score < min_val:
            min_val = score
        if score > max_val:
            max_val = score

    return min_val, max_val


min_score, max_score = get_min_max(scores)

print(f"Min: {min_score}, Max: {max_score}")