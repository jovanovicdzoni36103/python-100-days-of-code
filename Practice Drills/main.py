"""
=====================================================================
PYTHON + AI/ML PRACTICE ENGINE — main.py (TASK HUB)
=====================================================================

Ovo NIJE fajl za pokretanje. Ovo je instrukcioni hub - teorijska
pitanja, opisi zadataka, hintovi. NEMA gotovih rešenja.

REDOSLED:
1. THEORY CHECK — odgovori na sva pitanja PRE nego što diraš kod.
2. MINI CHALLENGES — brzi testovi, mogu u scratch.py.
3. PRACTICAL TASKS — svaki task ide u svoj fajl (npr.
   01_foundations/task_01.py).
4. AI/ML APPLICATION task.
5. Javi kad završiš oblast → generišem sledeću.

Pun raspored svih oblasti: ROADMAP.md
Trenutno aktivna oblast: AREA 1 — PYTHON FOUNDATIONS.
"""


# =====================================================================
# AREA 1 — PYTHON FOUNDATIONS
# Course Day 1-2 | AI/ML relevantnost: VISOKA
# =====================================================================


# ---------------------------------------------------------------------
# SECTION A — THEORY CHECK (uradi PRE praktičnog dela)
# ---------------------------------------------------------------------

"""
Odgovori svojim rečima (ne prepisuj definiciju) - objasni kao da
objašnjavaš nekome ko zna šta je AI model, ali ne zna Python.

1. Šta je promenljiva i zašto interpreter ne mora unapred da zna
   njen tip? Gde to pomaže, a gde može naškoditi u AI/ML kodu?
2. Razlika između int, float, str, bool? Zašto confidence score
   skoro nikad ne treba čuvati kao string?
3. Šta je type conversion i zašto JSON iz API-ja skoro uvek
   zahteva eksplicitnu konverziju pre matematike?
4. Razlika između `=` i `==`? Zašto zamena ne bi pukla odmah, ali
   bi pokvarila logiku negde dalje?
5. Šta se dešava ako sabereš string i int? Kad bi se ta greška
   realno pojavila pri čitanju fajla red po red?
6. Zašto je f-string bolji od `+` spajanja za prikaz predikcije?
7. Šta uvek vraća input()? Šta puca ako to zaboraviš dok učitavaš
   npr. "confidence threshold" od korisnika?
8. Razlika između int(x) i round(x) za float x? Primer iz ML
   konteksta gde to menja rezultat.
9. [DEBUG] TypeError: unsupported operand type(s) for +: 'int' and
   'str' pri sabiranju dve vrednosti "iz modela" - najverovatniji
   uzrok i kako bi proverio pre izmene koda?
10. [SCENARIO] API vrati {"confidence": "0.87"} - string, ne broj.
    Zašto je ovo čest slučaj i šta moraš da uradiš pre poređenja sa
    threshold-om 0.8?

Ne idi na Section B dok nemaš odgovor (makar radni) na svih 10.
"""


# ---------------------------------------------------------------------
# SECTION B — MINI LOGIC CHALLENGES
# ---------------------------------------------------------------------

"""
1. Confidence Rounder
   raw_confidence = "0.8734129" (string)
   → konvertuj u float, zaokruži na 2 decimale, ispiši "Confidence: 0.87"
   (bez if/else)

2. Token Cost Fixer
   Korisnik unosi broj tokena preko input() (uvek string).
   → konvertuj u int, pomnoži cenom 0.00002 po tokenu, ispiši sa 6 decimala.

3. Label Case Normalizer
   raw_label = "  Positive  "
   → .strip() skida razmake, .lower() prebacuje u mala slova
   → dobij tačno "positive"
"""


# ---------------------------------------------------------------------
# SECTION C — PRACTICAL TASKS
# ---------------------------------------------------------------------

"""
TASK 01 — Ispiši rezultat modela
Level 1 (najlakši)

Zadatak: Zamisli da si dobio rezultat od AI modela. Napravi 3
promenljive - ime modela, predikciju i confidence (broj) - i ispiši
ih u jednoj rečenici, jednim f-stringom.

Primer:
Model 'sentiment-v2' says: positive (confidence: 0.91)

Hint: f-string izgleda ovako - f"tekst {promenljiva} tekst"

(Usput: ovako svaki program prikazuje AI rezultat korisniku.)
"""

"""
TASK 02 — Očisti prljav tekst
Level 1 (lako)

Zadatak: Dobio si batch ID pun nepotrebnih razmaka, velikih slova i
podvlaka: "  BATCH_2024_A17  ". Očisti ga - makni razmake, prebaci u
mala slova, zameni "_" sa "-". Ne mora sve odjednom, može korak po
korak.

Primer:
"batch-2024-a17"

Hint: .strip() makne razmake, .lower() prebaci u mala slova,
.replace("_", "-") zameni podvlake crticama. Radi to redom.

(Usput: ovo je "čišćenje podataka" - prvi korak u skoro svakom AI
projektu.)
"""

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


# ---------------------------------------------------------------------
# SECTION D — AI/ML APPLICATION
# ---------------------------------------------------------------------

"""
TASK 04 — Koliko košta poziv AI modela
Level 3 (AI primena)

Zadatak: Hoćeš unapred da znaš koliko će koštati jedan poziv ka AI
modelu, na osnovu broja tokena. Cena se računa na 1000 tokena.

input_tokens = 1200
output_tokens = 350
price_per_1k_input = 0.003
price_per_1k_output = 0.015

Primer:
Estimated cost: $0.00885

Hint: prvo podeli tokene sa 1000, pa pomnoži cenom - posebno za
input, posebno za output, pa to dvoje saberi.

(Usput: ovako izgleda "cost tracking" u realnim AI automatizacijama.)
"""


# =====================================================================
# AREA 1 — WRAP UP
# =====================================================================

"""
Kada završiš theory check, mini challenges i task 01-04 → javi.
Generišem AREA 2 - CONTROL FLOW & RANDOMNESS (if/else, logički
operatori, random modul).
"""
