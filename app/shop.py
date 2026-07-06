from datetime import datetime


class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, cart: dict):
        total = 0
        for item, qty in cart.items():
            total += self.products[item] * qty
        return total

    def print_receipt(self, customer_name, cart: dict, total_cost: float):
        current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for item, qty in cart.items():
            price = self.products[item] * qty
            print(f"{qty} {item}s for {price:.2f} dollars")

        print(f"Total cost is {total_cost:.2f} dollars")
        print("See you again!")
