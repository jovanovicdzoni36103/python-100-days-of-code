"""
TASK 03 — Prosek dva modela
Level 2 (malo teže)

Zadatak: Dva modela su dala svoj confidence score. Nađi im prosek i
ispiši ga zaokružen na 3 decimale.

model_a_confidence = 0.812
model_b_confidence = 0.734

Primer:
Average ensemble confidence: 0.773

Hint: prosek = (a + b) / 2, a za zaokruživanje koristi round(broj, 3)

(Usput: ovo je najprostiji oblik "ensemble" pristupa u AI-ju.)
"""

# Napiši rešenje ispod ove linije:

model_a_confidence = 0.812
model_b_confidence = 0.734

average_models_confidence = round((model_a_confidence + model_b_confidence) / 2,3)
print(f"model_a_confidence: {model_a_confidence}\n"
      f"model_b_confidence: {model_b_confidence}\n"
      f"average_models_confidence: {average_models_confidence} ")