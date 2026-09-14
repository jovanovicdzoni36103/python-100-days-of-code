"""
TASK 03 - POST zahtev sa JSON telom                       [Level 4]

Pozovi https://jsonplaceholder.typicode.com/posts sa POST zahtevom.

Telo zahteva (JSON): {"title": "model-run", "body": "accuracy 0.91", "userId": 1}

Ispiši status kod i "id" iz odgovora.

Uslov: koristi requests.post(url, json=payload).

AI/ML: Slanje podataka modelu na obradu (npr. tekst za analizu, sliku za klasifikaciju) skoro uvek ide kroz POST zahtev sa JSON telom, ne kroz GET.
"""

# Rešenje:
