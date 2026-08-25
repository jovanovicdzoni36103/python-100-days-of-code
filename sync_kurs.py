#!/usr/bin/env python3
"""
sync_kurs.py

Prebacuje moj kod iz JetBrains Academy kursa u ovaj repo.

Dogovor:
  day_001 do day_004  moj stari kod, skripta ih ne dira nikad
  day_005 pa nadalje  dolazi iz kursa

Kurs i repo su isti folder. Kurs drzi kod dana koji trenutno radim
u folderu "Day N/task/".
Skripta ga kopira u day_00N/ ovog repoa. task.py postaje main.py,
ostali fajlovi zadrzavaju ime. solution.py se nikad ne kopira,
to je resenje autora kursa i ne ide na GitHub.

Koriscenje:
    python sync_kurs.py           pregled, nista se ne upisuje
    python sync_kurs.py 5         prebaci Day 5
    python sync_kurs.py all       prebaci sve dane koji imaju kod
    python sync_kurs.py all -y    isto, bez pitanja

Putanja do kursa se trazi ovim redom:
    1. promenljiva okruzenja KURS_PUTANJA
    2. fajl .kurs_putanja pored ove skripte
    3. sam ovaj folder, ako u njemu stoji course-info.yaml
    4. konstanta KURS ispod
"""

import difflib
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent

KURS = Path(r"C:\Users\PC\PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp")

# Dani koje sam vec odradio pre kursa. Ovde stoji moj stari kod i ostaje takav.
# Ako ikad hoces da i njih povuces iz kursa, izbaci broj iz ovog skupa.
ZAKLJUCANI_DANI = {1, 2, 3, 4}

NE_KOPIRAJ = {"solution.py", "__init__.py"}
PREIMENUJ = {"task.py": "main.py"}


def putanja_kursa() -> Path:
    iz_okruzenja = os.environ.get("KURS_PUTANJA", "").strip()
    if iz_okruzenja:
        return Path(iz_okruzenja)
    poseban = REPO / ".kurs_putanja"
    if poseban.is_file():
        tekst = poseban.read_text(encoding="utf-8-sig").strip()
        if tekst:
            return Path(tekst)
    if (REPO / "course-info.yaml").is_file():
        return REPO          # kurs i repo su spojeni u isti folder
    return KURS


def procitaj(p: Path) -> str:
    """Vrati sadrzaj bez BOM-a i sa LF prelomima."""
    sirovo = p.read_bytes().decode("utf-8-sig", errors="replace")
    return sirovo.replace("\r\n", "\n").replace("\r", "\n")


def ima_koda(tekst: str) -> bool:
    """False ako je fajl prazan ili samo komentari, tj. jos nista nisam napisao."""
    for red in tekst.splitlines():
        golo = red.strip()
        if golo and not golo.startswith("#"):
            return True
    return False


def je_sablon(tekst: str) -> bool:
    """Prazan day_NNN/main.py koji sam napravio unapred."""
    linije = [l.strip() for l in tekst.splitlines() if l.strip()]
    if not linije or len(linije) > 4:
        return False
    return all(
        l.startswith("#") or l.startswith('print("Zdravo, ovo je day_')
        for l in linije
    )


def dani_sa_kodom(kurs: Path):
    """Vrati [(broj_dana, folder_sa_kodom)] za dane koje sam otvorio u kursu."""
    nadjeno = []
    for folder in kurs.glob("Day *"):
        rep = folder.name[4:].strip()
        if not rep.isdigit():
            continue
        task = folder / "task"
        if task.is_dir():
            nadjeno.append((int(rep), task))
    return sorted(nadjeno)


def fajlovi_za_kopiranje(task: Path):
    for f in sorted(task.iterdir()):
        if not f.is_file():
            continue
        if f.name in NE_KOPIRAJ or f.name.startswith("task-"):
            continue
        if f.suffix in {".yaml", ".yml"}:
            continue
        yield f


def prikazi_razliku(staro: str, novo: str, ime: str, limit: int = 30):
    razlika = list(
        difflib.unified_diff(
            staro.splitlines(), novo.splitlines(), fromfile=ime, tofile="kurs", lineterm=""
        )
    )
    for red in razlika[:limit]:
        print("      " + red)
    if len(razlika) > limit:
        print(f"      ... jos {len(razlika) - limit} redova")


def obradi_dan(broj: int, task: Path, upisi: bool, bez_pitanja: bool) -> int:
    cilj_folder = REPO / f"day_{broj:03d}"
    upisano = 0

    for izvor in fajlovi_za_kopiranje(task):
        tekst = procitaj(izvor)
        if not ima_koda(tekst):
            continue

        ime = PREIMENUJ.get(izvor.name, izvor.name)
        cilj = cilj_folder / ime

        if cilj.exists():
            staro = procitaj(cilj)
            if staro == tekst:
                print(f"  Day {broj} -> {cilj.relative_to(REPO)}: isto, preskacem")
                continue
            oznaka = "prazan sablon" if je_sablon(staro) else "ima moj stariji kod"
            print(f"  Day {broj} -> {cilj.relative_to(REPO)}: razlicito ({oznaka})")
            if not je_sablon(staro):
                prikazi_razliku(staro, tekst, str(cilj.relative_to(REPO)))
        else:
            print(f"  Day {broj} -> {cilj.relative_to(REPO)}: nov fajl")

        if not upisi:
            continue

        if cilj.exists() and not je_sablon(procitaj(cilj)) and not bez_pitanja:
            odgovor = input(f"      prepisati {cilj.relative_to(REPO)}? [d/N] ").strip().lower()
            if odgovor not in {"d", "da", "y", "yes"}:
                print("      preskacem")
                continue

        cilj_folder.mkdir(parents=True, exist_ok=True)
        cilj.write_text(tekst, encoding="utf-8", newline="\n")
        print("      upisano")
        upisano += 1

    return upisano


def main() -> int:
    argumenti = list(sys.argv[1:])
    bez_pitanja = "-y" in argumenti or "--yes" in argumenti
    argumenti = [a for a in argumenti if a not in {"-y", "--yes"}]

    kurs = putanja_kursa()
    if not kurs.is_dir():
        print(f"Ne vidim folder kursa: {kurs}")
        print("Upisi tacnu putanju u .kurs_putanja pored ove skripte.")
        return 1

    svi_dani = dani_sa_kodom(kurs)
    if not svi_dani:
        print("Nijedan dan jos nema folder task/. Otvori dan u kursu pa probaj opet.")
        return 0

    if not argumenti:
        cilj_dani, upisi = svi_dani, False
        print("PREGLED. Nista se ne upisuje.")
        print("Za upis: python sync_kurs.py <broj dana>  ili  python sync_kurs.py all\n")
    elif argumenti[0] == "all":
        cilj_dani, upisi = svi_dani, True
    elif argumenti[0].isdigit():
        trazeni = int(argumenti[0])
        if trazeni in ZAKLJUCANI_DANI:
            print(f"Day {trazeni} je zakljucan. Tu stoji moj stari kod od pre kursa.")
            print("Ako stvarno hoces da ga prepises, izbaci broj iz ZAKLJUCANI_DANI u ovoj skripti.")
            return 1
        cilj_dani = [(b, t) for b, t in svi_dani if b == trazeni]
        if not cilj_dani:
            imam = ", ".join(str(b) for b, _ in svi_dani)
            print(f"Day {trazeni} nema folder task/. Otvoreni su mi: {imam}")
            return 1
        upisi = True
    else:
        print(__doc__)
        return 1

    zakljucani = sorted(b for b, _ in cilj_dani if b in ZAKLJUCANI_DANI)
    cilj_dani = [(b, t) for b, t in cilj_dani if b not in ZAKLJUCANI_DANI]

    print(f"Kurs: {kurs}")
    print(f"Repo: {REPO}")
    if zakljucani:
        spisak = ", ".join(f"Day {b}" for b in zakljucani)
        print(f"Zakljucano, ne diram: {spisak}  (tu je moj stari kod)")
    print()

    if not cilj_dani:
        print("Nema sta da se prebaci.")
        return 0

    ukupno = 0
    for broj, task in cilj_dani:
        ukupno += obradi_dan(broj, task, upisi, bez_pitanja)

    print()
    if upisi:
        print(f"Upisano fajlova: {ukupno}")
        if ukupno:
            print("Pogledaj izmene u gitu pa commituj.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
