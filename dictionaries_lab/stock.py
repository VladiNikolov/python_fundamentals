inventory = input().split()
inventory_product = {inventory[i]: inventory[i + 1] for i in range(0, len(inventory), 2)}

searched_product = input().split()

for product in searched_product:
    if product in inventory_product:
        print(f"We have {inventory_product[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
        