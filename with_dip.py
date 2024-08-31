from abc import ABC, abstractmethod

# Step 1: Abstraction
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Step 2: Implementations of different foods
class Pizza(Food):
    def prepare(self):
        print("Menyiapkan Pizza...")

class Burger(Food):
    def prepare(self):
        print("Menyiapkan Burger...")

class Kebab(Food):
    def prepare(self):
        print("Menyiapkan Kebab...")

# Step 3: High-level module (Restaurant) depending on abstraction
class Restaurant:
    def __init__(self, food: Food):
        self.food = food

    def order_food(self):
        self.food.prepare()

# Running the restaurant orders with different foods
print("Memesan Pizza:")
restaurant = Restaurant(Pizza())
restaurant.order_food()

print("\nMemesan Burger:")
restaurant = Restaurant(Burger())
restaurant.order_food()

print("\nMemesan Kebab:")
restaurant = Restaurant(Kebab())
restaurant.order_food()