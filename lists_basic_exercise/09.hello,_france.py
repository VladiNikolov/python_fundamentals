items_list = input().split("|")
budget = int(input())
sum = 0
my_list = []
for item in items_list:
    info_item = item.split("->")
    type_of_item = info_item[0]
    price = float(info_item[1])

    if type_of_item == "Clothes" and price <= 50:
        if budget >= price:
            budget -= price
            sum += price
            my_list.append(price)
    elif type_of_item == "Shoes" and price <= 35:
        if budget >= price:
            budget -= price
            sum += price
            my_list.append(price)
    elif type_of_item == "Accessories" and price <= 20.50:
        if budget >= price:
            budget -= price
            sum += price
            my_list.append(price)
for element in my_list:
    print(f"{element * 1.4:.2f}", end= " ")
print()
print(f"Profit: {(sum * 1.4) - sum:.2f}")
if budget + (sum * 1.4) >= 150:
    print("Hello, France!" )
else:
    print("Not enough money.")