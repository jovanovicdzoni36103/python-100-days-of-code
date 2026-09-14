# Python → AI/ML Curriculum - Master Structure

Izvor: kurs koji si poslao (604 lekcije, 102 sekcije, ~56h48m).
Redosled prati hronologiju kursa (Course Day). LEVEL i dubina
zadataka se određuju nezavisno od dana kursa - dan ti govori KADA
učiš koncept, LEVEL govori KOLIKO duboko ga vežbaš.

## Legenda AI/ML relevantnosti

- 🔴 VISOKA - direktno gradi AI/ML fundament, ne preskačati
- 🟡 SREDNJA - koristan opšti inženjerski koncept, obrađuje se normalno
- ⚪ NISKA - nije direktno vezano za AI/ML (uglavnom web dev/frontend) - preporučeno SKIMOVANJE, ne pun angažman

## Master grupisanje

| # | Oblast | Course Day (ref) | Ključni koncepti | Relevantnost | Level raspon |
|---|--------|-------------------|-------------------|---------------|--------------|
| 1 | Python Foundations | 1-2 | variables, data types, type conversion, operatori, f-strings, print/input | 🔴 | 1-4 |
| 2 | Control Flow & Randomness | 3-4 | if/elif/else, logički operatori, modulo, random modul | 🔴 | 1-4 |
| 3 | Loops & Iteration | 5-6 | for, range(), while, indentation | 🔴 | 1-4 |
| 4 | Functions I | 6, 8, 10 | def, parametri, positional/keyword args, return, docstrings | 🔴 | 1-5 |
| 5 | Data Structures: Lists & Dicts | 4, 9 | liste, nested liste, dictionaries, nested dict | 🔴 | 1-5 |
| 6 | Scope & Program Structure | 12 | local/global scope, konstante | 🟡 | 1-3 |
| 7 | Debugging Fundamentals | 13-14 | čitanje grešaka, print-debug, debugger | 🔴 | 2-4 |
| 8 | OOP Basics | 15-17 | klase, objekti, atributi, metode, `__init__` | 🔴 | 2-5 |
| 9 | OOP - Inheritance | 21 | class inheritance | 🟡 | 3-5 |
| 10 | Comprehensions | 26 | list/dict comprehension | 🔴 | 3-5 |
| 11 | Advanced Function Args | 27 | default values, `*args`, `**kwargs` | 🟡 | 3-4 |
| 12 | Exception Handling | 30 | try/except/finally, custom exceptions | 🔴 | 2-4 |
| 13 | Files, JSON, CSV | 24-25, 30 | file I/O, paths, JSON, CSV | 🔴 | 2-5 |
| 14 | APIs I - Basics | 33-34 | GET requests, JSON response, status codes | 🔴 | 2-5 |
| 15 | APIs II - Auth & REST | 35, 37, 66-67 | API keys, env variables, POST/PUT/DELETE, REST | 🔴 | 3-5 |
| 16 | Automation & Scheduling | 32, 36, 40 | datetime, scheduling, SMTP | 🟡 | 3-4 |
| 17 | Web Scraping | 45-48 | BeautifulSoup, Selenium | 🔴 (data collection) | 3-6 |
| 18 | Databases / SQL | 63, 69, 71 | SQLite, SQLAlchemy, CRUD | 🟡 | 3-5 |
| 19 | Git & Version Control | 70 | git, branching, github | 🟡 | 1-3 |
| 20 | ⚪ Web Dev Block (SKIM) | 41-62, 64-69 | HTML/CSS/Bootstrap/Flask/Jinja/WTForms | ⚪ | - |
| 21 | Pandas - Data Analysis | 72-76 | DataFrame, cleaning, grouping, merging, pivoting | 🔴 | 3-6 |
| 22 | Data Visualization | 73-76, 79 | Matplotlib, Seaborn, Plotly | 🔴 | 3-5 |
| 23 | NumPy | 77 | ndarray, broadcasting, matrix ops | 🔴 | 3-5 |
| 24 | Statistics & Regression | 78-80 | scikit-learn linear regression, statistička značajnost | 🔴 | 4-6 |

Napomena: oblast 20 namerno nema svoj folder u projektu - ne dobija
generisane zadatke dok se izričito ne zatraži.

## Kapstoni (posle svake veće celine)

- **Capstone 1** - posle oblasti 1-6 (Foundations → Scope): kombinuje
  variables, control flow, loops, functions, lists/dicts.
- **Capstone 2** - posle oblasti 7-12 (Debugging → Exceptions):
  OOP-centričan projekat sa error handling-om.
- **Capstone 3** - posle oblasti 13-16 (Files → Automation): pipeline
  koji čita/piše fajlove i zove eksterni API.
- **Capstone 4** - posle oblasti 17-19 (Scraping → Git): prikuplja
  podatke sa weba i čuva ih u bazi, verzionisano na Githubu.
- **Final Capstone** - posle oblasti 21-24 (Pandas → Regression):
  end-to-end mini data science projekat (clean → visualize → model →
  evaluate).

## ⚪ Šta se svesno skipuje/skimuje i zašto

Course Day 41-71 (~30 dana kursa) je web development blok: HTML,
CSS, Bootstrap, Flask, Jinja, WTForms, autentifikacija korisnika na
sajtu. To je ceo jedan "front-end/back-end web developer" trening
ugrađen u kurs - i skoro ništa od toga nije AI/ML.

Ono što VREDI zadržati iz tog bloka je ugrađeno u DRUGE oblasti,
umesto da dobije svoju:
- decorators (`@`) → reinforced kroz OOP (oblast 8)
- environment variables → reinforced kroz APIs II (oblast 15)
- SQL/SQLite → dobija svoju oblast (18), jer je opšte korisna
  veština za bilo koji data pipeline, ne samo za web app

Sve ostalo (HTML/CSS/Bootstrap/Flask templating/forme) - preskoči ili
prelistaj ubrzano. Ne troši vreme praveći ozbiljne vežbe tamo osim
ako imaš konkretan razlog (npr. praviš dashboard za model rezultate).

## Posle kursa (van obuhvata kursa, nastavak AI/ML puta)

scikit-learn dublje (klasifikacija, cross-validation) → feature
engineering → ML pipelines → model evaluation → deep learning →
PyTorch → LLMs / RAG / AI agenti. Ovo dolazi POSLE oblasti 24, kao
posebna faza kad kurs bude završen.

## Kako se ovo koristi (workflow)

1. `main.py` je jedini fajl koji čitaš za instrukcije. Trenutno
   sadrži Area 1.
2. Redosled unutar oblasti: theory check → mini challenges →
   practical tasks → AI/ML task → reflection questions.
3. Implementacija ide u odgovarajući folder (`01_foundations/`, itd.)
   - jedan fajl po tasku (`task_01.py`, `task_02.py`, ...).
4. Kad završiš oblast u celosti, javi - generiše se sledeća, sa
   istim standardom (theory check first, no solutions, AI/ML
   kontekst gde ima smisla).
5. Periodično (otprilike posle svake 3-4 oblasti) očekuj REVIEW
   SESSION koja kombinuje starije koncepte kroz novi AI/ML problem -
   to je namerno, ne greška u redosledu.
