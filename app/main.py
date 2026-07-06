import json
from datetime import datetime

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.gas_station import GasStation


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    gas_station = GasStation(data["FUEL_PRICE"])
    customers_data = data["customers"]
    shops_data = data["shops"]

    current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    for customer_data in customers_data:
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(
                customer_data["car"]["brand"],
                customer_data["car"]["fuel_consumption"]
            )
        )

        print(f"{customer.name} has {customer.money:.2f} dollars")

        options = []

        for shop_data in shops_data:
            shop = Shop(**shop_data)
            cost = customer.trip_cost(shop, gas_station.price)

            options.append((cost, shop))

            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{cost:.2f}"
            )

        cheapest_cost, cheapest_shop = min(options, key=lambda x: x[0])

        if not customer.enough_money(cheapest_cost):
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")

        customer.location = cheapest_shop.location

        products_cost = cheapest_shop.calculate_products_cost(
            customer.product_cart
        )

        print(f"\nDate: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for item, qty in customer.product_cart.items():
            item_cost = cheapest_shop.products[item] * qty
            print(f"{qty} {item}s for {item_cost:.2f} dollars")

        print(f"Total cost is {products_cost:.2f} dollars")

        total_cost = cheapest_cost
        customer.pay(total_cost)

        customer.location = [0, 0]

        print(f"\n{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()
