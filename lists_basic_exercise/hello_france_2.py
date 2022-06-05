items_with_their_prices = input().split("|")
budget = float(input())
sum_all_price = []
data_prices = []
profit = 0
new_price = 0
condition = False

for current_dress in items_with_their_prices:
    dress_info = current_dress.split("->")
    dress = dress_info[0]
    price = float(dress_info[1])
    condition = False

    if dress == "Clothes":
        if price <= 50:
            condition = True

    elif dress == "Shoes":
        if price <= 35:
            condition = True

    elif dress == "Accessories":
        if price <= 20.50:
            condition = True

    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            new_price = price + (price * 0.40)
            sum_all_price.append(new_price)
            data_prices.append(f"{new_price:.2f}")

print(" ".join(data_prices))
print(f"Profit: {profit:.2f}")
total_sum = budget + sum(sum_all_price)

if total_sum >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
