budget = float(input())
price_flour = float(input())
count_bread = 0
count_eggs = 0
pack_eggs_price = price_flour * 0.75
price_1l_milk = price_flour * 1.25
price_one_bread = price_flour + pack_eggs_price + (price_1l_milk /4)
while budget > price_one_bread:
    count_bread += 1
    budget = budget - price_one_bread
    count_eggs += 3
    if count_bread % 3 == 0:
        count_eggs = count_eggs - (count_bread - 2)

print(f"You made {count_bread} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")


