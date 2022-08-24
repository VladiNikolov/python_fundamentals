sum_without_taxes = 0
sum_with_taxes = 0
taxes = 0
total_price = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        break
    else:
        current_command = float(command)
        if current_command <= 0:
            print("Invalid price!")
            continue
        sum_without_taxes += current_command
        sum_with_taxes = sum_without_taxes * 1.2
        taxes = sum_with_taxes - sum_without_taxes

if command == "special":
    total_price = sum_with_taxes * 0.90
    if total_price <= 0:
        print("Invalid order!")
        exit()
    else:
        print('Congratulations you\'ve just bought a new computer!')
        print(f'Price without taxes: {sum_without_taxes :.2f}$')
        print(f'Taxes: {taxes :.2f}$')
        print('-----------')
        print(f'Total price: {total_price :.2f}$')
elif command == "regular":
    if sum_with_taxes <= 0:
        print("Invalid order!")
        exit()
    else:
        print('Congratulations you\'ve just bought a new computer!')
        print(f'Price without taxes: {sum_without_taxes :.2f}$')
        print(f'Taxes: {taxes :.2f}$')
        print('-----------')
        print(f'Total price: {sum_with_taxes :.2f}$')
