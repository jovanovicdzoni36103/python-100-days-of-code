"""
TASK 03 - super().__init__() i novi atribut               [Level 4]

Napravi podklasu RegressorModel(Model) koja pored name i accuracy ima
i dodatni atribut mse (mean squared error).

Uslov: pozovi super().__init__(name, accuracy) da postaviš nasleđene
atribute, pa dodaj self.mse = mse.

Napravi objekat i ispiši sva tri atributa.

AI/ML: Kad podklasa dodaje svoje specifične podatke (npr. regresija ima mse, a klasifikacija ima f1_score), super().__init__() ti čuva zajednički deo bez ponavljanja.
"""

# Rešenje:
