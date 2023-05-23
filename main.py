class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description} ({self.price} грн)"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_menu(self):
        print("Меню:")
        for item in self.items:
            print(item)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def add_menu_item(self, item):
        self.menu.add_item(item)

    def remove_menu_item(self, item):
        self.menu.remove_item(item)

    def display_menu(self):
        self.menu.display_menu()

    def place_order(self):
        print("Оформлення замовлення...")
        for item in self.order.items:
            print(item)
        total = self.order.calculate_total()
        print(f"Загальна сума: {total} грн")

    def save_order(self, filename):
        with open(filename, "w") as file:
            for item in self.order.items:
                file.write(str(item) + "\n")

pizza = FoodItem("Піца", "Смачна піца з сиром", 150)
salad = FoodItem("Салат", "Свіжий салат з овочів", 70)
soup = FoodItem("Суп", "Смачний гарячий суп", 90)

mmenu = Menu()
mmenu.add_item(pizza)
mmenu.add_item(salad)
mmenu.add_item(soup)

zakaz = Order()
zakaz.add_item(піца)
zakz.add_item(суп)

nikas = Restaurant()
nikas.menu = mmenu

nikas.display_menu()

nikas.order = zakaz
nikas.place_order()
