"""
TASK 06 - Spoji dva DataFrame-a                           [Level 6]

Dato:   models = pd.DataFrame({"id": [1, 2, 3], "name": ["a", "b", "c"]})
        results = pd.DataFrame({"id": [1, 2, 3], "accuracy": [0.81, 0.65, 0.93]})

Spoji ih u jedan DataFrame po koloni "id", tako da svaki red ima i
name i accuracy.

Uslov: koristi pd.merge(models, results, on="id").

AI/ML: Podaci o modelima i njihovi rezultati često dolaze iz dva različita izvora (npr. jedan fajl sa konfiguracijom, drugi sa metrikama). merge() ih spaja u jednu tabelu za analizu.
"""

# Rešenje:
