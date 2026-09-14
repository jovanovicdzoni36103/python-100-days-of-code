"""
TASK 04 - Proveri status kod pre parsiranja               [Level 5]

Pozovi: https://jsonplaceholder.typicode.com/todos/9999999 (ne postoji)

Proveri status_code pre nego što pozoveš .json(). Ako nije 200,
ispiši "Request failed with status {status_code}" i ne pokušavaj
dalje da parsiraš odgovor.

AI/ML: Model ili API mogu vratiti grešku (npr. 404, 500) umesto očekivanog rezultata. Ne proveravati status kod pre parsiranja je čest uzrok padova u produkciji.
"""

# Rešenje:
