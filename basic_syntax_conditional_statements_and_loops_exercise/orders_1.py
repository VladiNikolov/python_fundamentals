number_of_orders = int(input())
total_price = 0

for _ in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    needed_capsules = int(input())
    if 0.01 <= price_capsule <= 100:
        if 1 <= days <= 31:
            if 1 <= needed_capsules <= 2000:
                price = price_capsule * days * needed_capsules
                total_price += price
                print(f"The price for the coffee is: ${price:.2f}")
    else:
        continue
print(f"Total: ${total_price:.2f}")