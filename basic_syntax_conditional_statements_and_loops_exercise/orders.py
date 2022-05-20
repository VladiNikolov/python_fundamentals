number_of_orders = int(input())
all_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsule_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= needed_capsule_per_day <= 2000:
        price = price_per_capsule * days * needed_capsule_per_day
        all_price += price
        print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${all_price:.2f}")
