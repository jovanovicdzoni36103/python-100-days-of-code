class MenuItem:
    def __init__(self, name: str, cost: float, ingredients: dict):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 1.5, {"water": 50, "milk": 0, "coffee": 18}),
            MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24}),
            MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24}),
        ]

    def get_items(self) -> str:
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.rstrip("/")

    def find_drink(self, order_name: str) -> MenuItem | None:
        for item in self.menu:
            if item.name.lower() == order_name.lower():
                return item
        print("Sorry, that item is not available.")
        return None