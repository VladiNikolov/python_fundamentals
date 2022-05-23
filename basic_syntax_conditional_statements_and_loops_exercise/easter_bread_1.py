budget = float(input())
price_1kg_flour = float(input())

count_loaf = 0
count_egg = 0
price_eggs = price_1kg_flour * 0.75
price_milk = price_1kg_flour * 1.25
price_one_loaf = price_1kg_flour + price_eggs + (price_milk / 4)
while budget > price_one_loaf:
    budget -= price_one_loaf
    count_loaf += 1
    count_egg += 3
    if count_loaf % 3 == 0:
        count_egg = count_egg - (count_loaf - 2)
print(f"You made {count_loaf} loaves of Easter bread! Now you have {count_egg} eggs and {budget:.2f}BGN left.")






