def orders_function(products: str, number: int):
    if products == "coffee":
        price = 1.50
        return price * quantity
    elif products == "coke":
        price = 1.40
        return price * quantity
    elif products == "water":
        price = 1.00
        return price * quantity
    elif products == "snacks":
        price = 2.00
        return price * quantity

product_type = input()
quantity = int(input())
result = orders_function(product_type, quantity)
print(f"{result:.2f}")

