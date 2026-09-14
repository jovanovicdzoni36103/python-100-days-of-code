"""
PYTHON + AI/ML PRACTICE ENGINE
Aktivan blok: AREA 1 - Python Foundations | Course Day 1-2 | 🔴 VISOKA relevantnost

Redosled: Theory → Mini Challenges → Tasks → javi → Area 2.
Detaljan raspored: ROADMAP.md
"""


# ──────────────────────────────────────────
# A - THEORY  (odgovori PRE kodiranja)
# ──────────────────────────────────────────
"""
1.  Promenljiva - šta je i zašto Python ne zahteva unapred tip?
    Gde to može biti problem u AI/ML kodu?

2.  int / float / str / bool - razlika između tipova u jednoj rečenici.
    Zašto confidence score ne sme biti string?

3.  Type conversion - šta je i zašto JSON iz API-ja zahteva
    eksplicitnu konverziju pre matematike?

4.  = vs == - koja je razlika? Šta se dešava ako ih zameniš?

5.  input() - šta uvek vraća? Kako to kvari threshold poređenje?
"""


# ──────────────────────────────────────────
# B - MINI CHALLENGES  (scratch.py ili direktno ovde)
# ──────────────────────────────────────────
"""
1.  raw = "0.8734129"
    → ispiši: Confidence: 0.87   (float konverzija + round na 2 dec)

2.  tokens = input("Broj tokena: ")
    → ispiši cenu  (cena po tokenu: 0.00002, prikaz sa 6 decimala)

3.  "  Positive  "  →  "positive"
    (.strip() + .lower())
"""


# ──────────────────────────────────────────
# C - TASKS  (01_foundations/task_XX.py)
# ──────────────────────────────────────────
"""
TASK 01 - Ispiši rezultat modela                         [Level 1]
Imaš: ime modela, predikcija, confidence.
Ispiši jednim f-stringom.

Izlaz:  Model 'sentiment-v2' says: positive (confidence: 0.91)
Hint:   f"Model '{model}' says: {pred} (confidence: {conf})"

AI/ML: Ovako svaki program prikazuje izlaz modela korisniku.
"""

"""
TASK 02 - Očisti batch ID                                [Level 1]
Dato:   "  BATCH_2024_A17  "
Cilj:   "batch-2024-a17"

Koraci: .strip() → .lower() → .replace("_", "-")

AI/ML: Data cleaning - obavezan prvi korak u svakom ML pipeline-u.
"""

"""
TASK 03 - Prosek dva modela                              [Level 2]
model_a = 0.812
model_b = 0.734

Nađi prosek, zaokruži na 3 decimale.
Izlaz: Average ensemble confidence: 0.773

AI/ML: Ensembling - kombinovanje predikcija više modela za bolji rezultat.
"""

"""
TASK 04 - Cena jednog API poziva                         [Level 3]
input_tokens  = 1200   |  price_per_1k_input  = 0.003
output_tokens = 350    |  price_per_1k_output = 0.015

Izračunaj ukupnu cenu.
Izlaz: Estimated cost: $0.00885

AI/ML: Cost tracking - bez ovoga ne možeš znati profitabilnost automatizacije.
"""


# ──────────────────────────────────────────
# Završi sve → javi → generišem AREA 2.
# ──────────────────────────────────────────
