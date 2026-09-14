"""
TASK 03 - finally: obavezno zatvaranje resursa            [Level 3]

Napravi funkciju process_batch(data) koja ispisuje "Processing..." pa
namerno baca grešku (npr. deljenje sa nulom) ako je data prazna lista.

U finally bloku ispiši "Batch closed", bez obzira da li je greška
nastala.

Testiraj sa praznom i sa nepraznom listom.

AI/ML: finally se koristi kad nešto MORA da se izvrši bez obzira na grešku, npr. zatvaranje konekcije ka bazi ili API-ju posle obrade batch-a.
"""

# Rešenje:
