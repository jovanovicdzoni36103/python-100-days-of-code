"""
TASK 04 - Custom exception za nevalidan score             [Level 4]

Napravi klasu InvalidScoreError koja nasleđuje Exception.

Napravi funkciju validate_score(score) koja baca InvalidScoreError
ako score nije između 0 i 1. U suprotnom vraća score.

Testiraj sa score=1.5 (uhvati grešku i ispiši poruku) i sa score=0.8.

AI/ML: Custom exception ti omogućava da jasno imenuješ šta je tačno pošlo po zlu (nevalidan score), umesto da se oslanjaš na generičke Python greške.
"""

# Rešenje:
