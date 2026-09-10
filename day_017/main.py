"""
===========================================================
VELIKI LAKI OOP PROJEKAT — MINI KVIZ
===========================================================

CILJ:

Napravi mali Python Quiz program koristeći OOP i više fajlova.

Projekat treba da bude jednostavan, ali da kroz njega ponoviš:

- klase i objekte
- __init__()
- atribute
- metode
- self
- menjanje atributa
- rad sa više objekata
- listu objekata
- import klasa iz drugih fajlova
- organizaciju projekta u više fajlova
- jednostavan Python paket sa PyPI-ja

NEMOJ praviti komplikovan projekat.
Poenta je da razumeš kako delovi zajedno rade.


===========================================================
STRUKTURA PROJEKTA
===========================================================

Napravi sledeće fajlove:

quiz_project/
│
├── main.py
├── question.py
├── quiz.py
├── player.py
└── data.py


Svaki fajl ima svoju odgovornost.


===========================================================
1. question.py
===========================================================

Napravi klasu:

Question

Klasa treba da ima:

- text
- answer

Kada napraviš objekat:

Question("Koji je glavni grad Srbije?", "Beograd")

treba da dobiješ Question objekat koji u sebi čuva pitanje
i tačan odgovor.

OBAVEZNO koristi:

- class
- __init__()
- self
- atribute


-----------------------------------------------------------
ZADATAK
-----------------------------------------------------------

Napravi klasu Question.

Dodaj __init__().

Sačuvaj:

self.text
self.answer


===========================================================
2. data.py
===========================================================

Ovaj fajl treba da sadrži sva pitanja.

Importuj Question klasu iz question.py.

Napravi najmanje 5 Question objekata.

Na primer:

Question(
    "Koji je glavni grad Srbije?",
    "Beograd"
)

Question(
    "Koliko je 2 + 2?",
    "4"
)

...

Na kraju napravi listu:

questions = [
    question1,
    question2,
    question3,
    ...
]


CILJ:

Da data.py bude mesto gde se čuvaju sva pitanja.


===========================================================
3. player.py
===========================================================

Napravi klasu:

Player

Player treba da ima:

- name
- games_played

U __init__():

games_played treba da bude 0.

Dodaj metodu:

play_game()

Ova metoda treba da poveća games_played za 1.


Na primer:

player.play_game()

treba da promeni:

0 -> 1

-----------------------------------------------------------
BONUS
-----------------------------------------------------------

Dodaj još jednu metodu:

show_stats()

Ona treba da ispiše koliko je igara igrač odigrao.


===========================================================
4. quiz.py
===========================================================

Ovo je glavna klasa projekta.

Napravi:

class Quiz


Quiz treba da ima najmanje:

- questions
- current_question
- score
- quiz_name

U __init__():

questions dobija listu pitanja.

current_question počinje od 0.

score počinje od 0.

quiz_name može biti:

"Python Beginner Quiz"


-----------------------------------------------------------
5. METODA next_question()
-----------------------------------------------------------

U Quiz klasi napravi:

next_question()


Metoda treba da:

1. Uzme trenutno pitanje iz liste.
2. Prikaže ga korisniku.
3. Zatraži odgovor preko input().
4. Proveri odgovor.
5. Pomeri se na sledeće pitanje.


Na primer:

Q1. Koji je glavni grad Srbije?
Tvoj odgovor:


VAŽNO:

Koristi:

self.current_question


i posle pitanja povećaj:

self.current_question += 1


===========================================================
6. METODA check_answer()
===========================================================

U Quiz klasi napravi:

check_answer(user_answer, correct_answer)


Ako je odgovor tačan:

- ispiši "Tačno!"
- povećaj score za 1

Ako nije:

- ispiši "Netačno!"
- ispiši tačan odgovor.


Na primer:

Tačno!

ili:

Netačno!
Tačan odgovor je: Beograd


===========================================================
7. METODA show_score()
===========================================================

Dodaj:

show_score()


Ona treba da prikaže:

Rezultat: 4/5


Nemoj komplikovati.


===========================================================
8. METODA has_more_questions()
===========================================================

Dodaj još jednu malu metodu:

has_more_questions()


Treba da vrati:

True

ako još postoji pitanje.


Treba da vrati:

False

kada su sva pitanja završena.


Ovo ćeš koristiti u main.py.


===========================================================
9. main.py
===========================================================

Ovo je fajl koji pokreće ceo program.

Importuj:

- Quiz iz quiz.py
- Player iz player.py
- questions iz data.py


-----------------------------------------------------------
POČETAK PROGRAMA
-----------------------------------------------------------

Prvo pitaj korisnika:

"Unesi ime: "


Napravi Player objekat.


Na primer:

player = Player(name)


Zatim napravi Quiz objekat koristeći listu pitanja.


Na primer:

quiz = Quiz(questions)


-----------------------------------------------------------
POKRETANJE KVIZA
-----------------------------------------------------------

Prikaži ime kviza.

Na primer:

==============================
Python Beginner Quiz
==============================


Zatim koristi while petlju.

Dok ima još pitanja:

quiz.next_question()


Kada nema više pitanja:

- prikaži konačan rezultat
- povećaj broj odigranih igara
- prikaži statistiku igrača


Na primer:

Quiz završen!

Rezultat: 4/5

Igrač: Nikola
Odigranih igara: 1


===========================================================
10. DIREKTNA PROMENA ATRIBUTA
===========================================================

Pre pokretanja kviza probaj ručno da promeniš neki atribut
objekta.

Na primer:

player.games_played = 10

Ispiši njegovu vrednost.

Posle toga postavi je ponovo na 0.


CILJ:

Da vidiš da atribut objekta možeš direktno menjati.


===========================================================
11. PYPI PAKET
===========================================================

Instaliraj jedan jednostavan paket sa PyPI-ja.

Predlog:

colorama


Instalacija:

pip install colorama


Zatim ga importuj u projektu.

Iskoristi ga samo za nekoliko print() naredbi.

Na primer:

naslov kviza
"Tačno!"
"Netačno!"


NE TROŠI VREME NA KOMPLIKOVANJE OVOGA.


===========================================================
12. KAKO TREBA DA IZGLEDA PROJEKAT
===========================================================

Primer organizacije:

quiz_project/

    main.py

    question.py
        -> Question klasa

    quiz.py
        -> Quiz klasa

    player.py
        -> Player klasa

    data.py
        -> lista Question objekata


Glavna ideja:

data.py
    ↓
Question objekti
    ↓
Quiz
    ↓
main.py


Player je dodatni objekat koji prati igrača.


===========================================================
13. PRIMER KAKO PROGRAM TREBA DA RADI
===========================================================

==============================
Python Beginner Quiz
==============================

Unesi ime: Nikola

Q1. Koji je glavni grad Srbije?
Tvoj odgovor: Beograd

Tačno!

Q2. Koliko je 2 + 2?
Tvoj odgovor: 5

Netačno!
Tačan odgovor je: 4

Q3. Koji programski jezik učimo?
Tvoj odgovor: Python

Tačno!


Quiz završen!

Rezultat: 2/3

Igrač: Nikola
Odigranih igara: 1



===========================================================
"""

from player import Player
from quiz import Quiz
from data import questions


user_name = input("Enter your name: ")
user = Player(user_name)

quiz_obj = Quiz(questions)

print(f"\n{quiz_obj.quiz_name}")

while quiz_obj.has_more_questions():
    print(quiz_obj.next_question())

user.play_game()

print("\nQuiz finished!")
print(f"Player: {user.name}")
print(f"Score: {quiz_obj.score}/{len(questions)}")
print(f"Games played: {user.show_stats()}")