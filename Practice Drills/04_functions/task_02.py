"""
TASK 02 - Function with default parameter value            [Level 2]

Create a function normalize_score(score, decimals=2) that rounds
score to the given number of decimal places. If decimals is not provided, use 2.

Call it twice: once without decimals, once with decimals=4.

Given: score = 0.873456

AI/ML: Score processing functions almost always have default values (e.g. number of decimals, rounding threshold), so you don't have to specify them every time.
"""

score = 0.873456

def normalize_score(score, decimals=2):
    return round(score, decimals)
result1 = normalize_score(score)
print(f"Bez decimals: {result1}")

result2 = normalize_score(score, decimals=4)
print(f"Sa decimals=4: {result2}")