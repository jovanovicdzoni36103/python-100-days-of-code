"""
TASK 03 - Pronađi zašto je prosek pogrešan                [Level 3]

Ovaj kod ne baca grešku, ali daje pogrešan rezultat:

scores = [0.8, 0.6, 0.9, 0.7]
total = 0
for s in scores:
    total += s
average = total / 3

print(f"Average: {average}")

Pronađi grešku i popravi je tako da average bude tačan prosek.

AI/ML: Greške koje ne bacaju exception, nego samo daju pogrešan broj (kao ovde pogrešan imenilac), su opasnije od pravih grešaka jer lako prođu neprimećeno u evaluaciji modela.
"""

# Rešenje:
