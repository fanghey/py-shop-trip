from datetime import datetime

current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

for customer_data in customers_date:
    customer = Customer(...)

    print(f"{customer.name} has {customer.money:.2f} dollars")

    options = []

    for shop_data in shops_date:
        shop = Shop(**shop_data)

        cost = customer.costs_for_trip_to_shop(shop, gas_station.price)
        options.append((cost, shop))

        print(f"{customer}'s trip to the {shop} costs {cost:.2f}")

    cheapest_cost, cheapest_shop = min(options, key=lambda x: x[0])

    if not customer.enough_money(cheapest_cost):
        print(f"{customer} doesn't have enough money to make a purchase in any shop")
        continue

    print(f"{customer} rides to {cheapest_shop}")

    customer.location = cheapest_shop.location

    print(f"\nDate: {current_time}")
    print(f"Thanks, {customer}, for your purchase!")

    print(customer.get_receipts(cheapest_shop))

    customer.location = "home"

    print(f"\n{customer} rides home")
    print(f"{customer} now has {customer.calculate_wallet(cheapest_cost):.2f} dollars")
