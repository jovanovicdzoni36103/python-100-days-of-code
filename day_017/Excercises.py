# ============================================================
# ZADATAK 1 — Student Class
# ============================================================
# Napravi klasu Student.
#
# Student treba da ima:
# - name
# - age
# - grade
#
# Napravi nekoliko Student objekata.
# Prikaži njihove podatke.
#
# Zatim promeni grade jednog studenta
# i ponovo prikaži njegove podatke.
#
# Cilj:
# Vežbaj razliku između klase, objekta i atributa.
# Posebno obrati pažnju na to da svaki objekat ima
# svoje nezavisne vrednosti.

# RESENJE

# class Student(object):
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old and his grade is {self.grade}"
#
# najbolji = Student('Nikola', 22, 8.42)
# najgori = Student('Nenad', 24, 7.15)
#
# najbolji.grade = 9
#
# print(najbolji)
# print(najgori)


# ============================================================
# ZADATAK 2 — Bank Account
# ============================================================
# Napravi klasu BankAccount.
#
# Atributi:
# - owner
# - balance
#
# Metode:
# - deposit(amount)
# - withdraw(amount)
# - show_balance()
#
# deposit treba da poveća balance.
# withdraw treba da smanji balance samo ako korisnik ima dovoljno novca.
#
# Napravi najmanje 3 računa.
# Testiraj različite transakcije na svakom računu.
#
# Cilj:
# Nauči da metoda menja stanje konkretnog objekta.

# RESENJE

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Uplaćeno {amount} RSD na račun korisnika {self.owner}.")
#         else:
#             print("Iznos uplate mora biti veći od 0.")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Iznos za podizanje mora biti veći od 0.")
#         elif amount <= self.balance:
#             self.balance -= amount
#             print(f"Podignuto {amount} RSD sa računa korisnika {self.owner}.")
#         else:
#             print(f"Transakcija odbijena: Nedovoljno sredstava na računu ({self.owner}).")
#
#     def show_balance(self):
#         print(f"Trenutno stanje na računu ({self.owner}): {self.balance} RSD\n")
#
#
# racun1 = BankAccount("Nikola", 500)
# racun2 = BankAccount("Lazar", 1200)
# racun3 = BankAccount("Uros", 100)
#
# racun1.show_balance()
# racun1.deposit(1000)
# racun1.withdraw(300)
# racun1.show_balance()
#
# racun2.show_balance()
# racun2.withdraw(2000)
# racun2.show_balance()
#
# racun3.deposit(500)
# racun3.show_balance()


# ============================================================
# ZADATAK 3 — Dog System
# ============================================================
# Napravi klasu Dog.
#
# Atributi:
# - name
# - breed
# - age
# - energy
#
# Napravi metode:
# - bark()
# - eat()
# - run()
# - sleep()
#
# energy treba da se menja zavisno od akcije.
#
# Na primer:
# - run smanjuje energy
# - eat povećava energy
# - sleep povećava energy
#
# Napravi više pasa i testiraj metode nad različitim objektima.

# RESENJE

# class Dog(object):
#     def __init__(self, name, energy):
#         self.name = name
#         self.energy = energy
#
#
#
#     def bark(self):
#         print("bark")
#
#     def eat(self):
#         self.energy += 5
#         print("eat")
#
#     def run(self):
#         self.energy -= 10
#         print("run")
#
#     def sleep(self):
#         self.energy += 15
#         print("sleep")
#
# vojnicki = Dog("dzeki", 100)
# vojnicki.run()
# vojnicki.eat()
# vojnicki.sleep()
#
# print(f"energija kera je {vojnicki.energy}")



# ============================================================
# ZADATAK 3 — Restaurant Order
# ============================================================
# Napravi klase:
# - MenuItem
# - Order
#
# MenuItem:
# - name
# - price
#
# Order:
# - order_id
# - items
# - status
#
# Order metode:
# - add_item(item)
# - remove_item(item_name)
# - calculate_total()
# - change_status(new_status)
# - show_order()
#
# Statusi mogu biti:
# - pending
# - preparing
# - ready
# - delivered
# - cancelled
#
# Dodaj validaciju statusa.
#
# Cilj:
# Vežbaj objekte koji sadrže listu drugih objekata
# i metode koje menjaju stanje.

# RESENJE

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    VALID_STATUSES = ["pending", "preparing", "ready", "delivered", "cancelled"]

    def __init__(self, order_id, items=None, status="pending"):
        self.order_id = order_id
        self.items = items if items is not None else []
        self.status = status if status in self.VALID_STATUSES else "pending"

    def add_item(self, item):
        self.items.append(item)
        print(f"Dodato: {item.name} ({item.price} RSD)")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Uklonjeno: {item.name}")
                return
        print(f"Stavka '{item_name}' nije pronađena u narudžbini.")

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def change_status(self, new_status):
        if new_status in self.VALID_STATUSES:
            self.status = new_status
            print(f"Status narudžbine #{self.order_id} promenjen u: {self.status}")
        else:
            print(f"Nevažeći status: '{new_status}'. Dozvoljeni statusi su: {self.VALID_STATUSES}")

    def show_order(self):
        print("\n" + "=" * 30)
        print(f"NARUDŽBINA #{self.order_id}")
        print(f"Status: {self.status}")
        print("Stavke:")
        if not self.items:
            print("  (Prazna narudžbina)")
        else:
            for item in self.items:
                print(f"  - {item.name}: {item.price} RSD")
        print(f"Ukupno za plaćanje: {self.calculate_total()} RSD")
        print("=" * 30 + "\n")



pica = MenuItem("Capricciosa", 950)
coka_kola = MenuItem("Coca-Cola 0.33", 220)
palacinka = MenuItem("Palačinka sa Nutelom", 380)

narudzbina_1 = Order(order_id=101)

narudzbina_1.add_item(pica)
narudzbina_1.add_item(coka_kola)
narudzbina_1.add_item(palacinka)

narudzbina_1.show_order()

narudzbina_1.change_status("preparing")
narudzbina_1.change_status("invalid_status")

narudzbina_1.remove_item("Coca-Cola 0.33")
narudzbina_1.show_order()