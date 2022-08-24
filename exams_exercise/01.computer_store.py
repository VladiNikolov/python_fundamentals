total_sum = 0
command = input()

while not command == "special" and not command == "regular":
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
    else:
        total_sum += current_price

    command = input()

taxes = total_sum * 0.20
price_whit_discount = total_sum + taxes
if command == "special":
    price_whit_discount = (total_sum + taxes) * 0.90


if total_sum == 0:
    print("Invalid order!")
else:
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_sum :.2f}$')
    print(f'Taxes: {taxes :.2f}$')
    print('-----------')
    print(f'Total price: {price_whit_discount :.2f}$')


