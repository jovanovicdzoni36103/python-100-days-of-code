"""
TASK 05 - Jedna klasa kao atribut druge                   [Level 5]

Koristeći klasu Model, napravi klasu Experiment sa
__init__(self, name, model) koja čuva self.name i self.model.

Dodaj metodu report() koja vraća string:
Izlaz:  Experiment 'exp-01' used model 'sentiment-v2' (accuracy: 0.87)

Napravi Model objekat, pa Experiment objekat koji ga koristi, i pozovi
report().

AI/ML: Eksperiment u ML-u je uvek više od samog modela: ima ime, datum, konfiguraciju. Composition (klasa unutar klase) je način da to predstaviš u kodu.
"""

# Rešenje:
