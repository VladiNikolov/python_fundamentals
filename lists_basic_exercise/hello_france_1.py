items_with_their_prices = input().split("|")
budget = int(input())
sum_all_bye = 0

my_list = []
for current_item in items_with_their_prices:
    info_item = current_item.split("->")
    items = info_item[0]
    price = float(info_item[1])

    if items == "Clothes" and price <= 50 and budget >= price:
        budget -= price
        sum_all_bye += price
        my_list.append(f"{price * 1.4:.2f}")
    elif items == "Shoes" and price <= 35 and budget >= price:
        budget -= price
        sum_all_bye += price
        my_list.append(f"{price * 1.4:.2f}")
    elif items == "Accessories" and price <= 20.50 and budget >= price:
        budget -= price
        sum_all_bye += price
        my_list.append(f"{price * 1.4:.2f}")
sum_with_profit = sum_all_bye * 1.4
profit = sum_with_profit - sum_all_bye
print(f" ".join(my_list))
print(f"Profit: {profit:.2f}")
if sum_with_profit + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
