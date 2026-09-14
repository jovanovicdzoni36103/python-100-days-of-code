"""
TASK 04 - Nested dict: metrike više modela                [Level 4]

Napravi rečnik results gde je ključ ime modela, a vrednost rečnik sa
"accuracy" i "f1_score".

Primer strukture:
results = {
    "model_a": {"accuracy": 0.81, "f1_score": 0.79},
    "model_b": {"accuracy": 0.88, "f1_score": 0.85},
}

Ispiši ime modela sa najvećom accuracy vrednošću.

AI/ML: Kad upoređuješ više eksperimenata, rezultati se prirodno organizuju kao rečnik rečnika: model -> njegove metrike. Ovo je osnova za kasnije poređenje u pandas-u.
"""

# Rešenje:
