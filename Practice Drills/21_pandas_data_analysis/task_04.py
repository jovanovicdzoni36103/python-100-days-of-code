"""
TASK 04 - Prosečna accuracy po tipu modela                [Level 4]

Dato:   data = {
            "type": ["classifier", "classifier", "regressor", "regressor"],
            "accuracy": [0.81, 0.77, 0.90, 0.85],
        }

Grupiši po koloni "type" i izračunaj prosečnu accuracy za svaku grupu.

Uslov: koristi df.groupby("type")["accuracy"].mean().

AI/ML: Groupby je kako upoređuješ performanse po kategorijama (tip modela, dataset, verzija) umesto da gledaš svaki red pojedinačno.
"""

# Rešenje:
