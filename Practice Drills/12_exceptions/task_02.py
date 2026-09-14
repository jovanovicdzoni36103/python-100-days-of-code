"""
TASK 02 - Uhvati ZeroDivisionError                        [Level 3]

Napravi funkciju safe_accuracy(correct, total) koja vraća
correct / total, a ako je total 0, vraća 0.0 umesto da program pukne.

Testiraj je sa total=0 i sa total=10.

Uslov: koristi try/except ZeroDivisionError.

AI/ML: Accuracy nema smisla računati kad nemaš nijedan uzorak (total=0), a to se realno dešava kad je batch prazan. Funkcija ne sme da sruši ceo pipeline zbog toga.
"""

# Rešenje:
