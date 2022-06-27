number_of_cities = int(input())


profit = 0
total_profit = 0
for city in range(1, number_of_cities + 1):
    name_of_city = input()
    owner_income = float(input())
    owner_expenses = float(input())

    if city % 5 == 0:
        profit = (owner_income * 0.90) - owner_expenses
    elif city % 3 == 0:
        profit = owner_income - (owner_expenses * 1.5)
    else:
        profit = owner_income - owner_expenses
    print(f"In {name_of_city} Burger Bus earned {profit:.2f} leva.")
    total_profit += profit
print(f"Burger Bus total profit: {total_profit:.2f} leva.")




