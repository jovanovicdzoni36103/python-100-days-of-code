"""
TASK 04 - Print-debug: pogrešan broj filtriranih uzoraka  [Level 4]

Ovaj kod treba da zadrži samo uzorke sa accuracy > 0.7, ali vraća
pogrešan broj uzoraka:

samples = [0.65, 0.72, 0.81, 0.55, 0.90, 0.68]
kept = []
for s in samples:
    if s > 0.7:
        kept.append(s)
    kept.append(s)

print(f"Kept: {len(kept)} of {len(samples)}")

Dodaj print() linije da vidiš šta se dešava unutar petlje, pronađi
grešku i popravi je.

AI/ML: Pogrešna indentacija ili pogrešno mesto jedne linije u petlji za filtriranje je čest uzrok kad dataset posle 'čišćenja' ima više redova nego što treba.
"""

# Rešenje:
