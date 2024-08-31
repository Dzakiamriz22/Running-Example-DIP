class Pizza:
    def prepare(self):
        print("Menyiapkan Pizza...")

class Burger:
    def prepare(self):
        print("Menyiapkan Burger...")

class Kebab:
    def prepare(self):
        print("Menyiapkan Kebab...")

class Restaurant:
    def __init__(self):
        self.pizza = Pizza()
        self.burger = Burger()
        self.kebab = Kebab()

    def order_pizza(self):
        self.pizza.prepare()

    def order_burger(self):
        self.burger.prepare()

    def order_kebab(self):
        self.kebab.prepare()

# Running the restaurant orders
restaurant = Restaurant()
restaurant.order_pizza()
restaurant.order_burger()
restaurant.order_kebab()
