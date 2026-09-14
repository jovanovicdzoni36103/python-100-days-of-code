"""
TASK 02 - Popravi IndexError u petlji                     [Level 2]

Ovaj kod baca grešku:

scores = [0.5, 0.7, 0.9]
for i in range(len(scores) + 1):
    print(scores[i])

Pokreni ga, pročitaj traceback, pronađi tačan red gde je problem i
popravi ga.

AI/ML: IndexError zbog petlje koja ide jedan korak predaleko (off-by-one) je čest bag kad obrađuješ listu predikcija ili redove dataseta.
"""

# Rešenje:
