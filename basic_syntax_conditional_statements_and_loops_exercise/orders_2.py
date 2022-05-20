orders_number = int(input())

all_price = 0
i = 0
while i < orders_number:
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= needed_capsules_per_day <= 2000:
        price = price_per_capsule * days * needed_capsules_per_day
        all_price = all_price + price
        print(f"The price for the coffee is: ${price:.2f}")
    i += 1
print(f"Total: ${all_price:.2f}")