products = input()
product_quantity = int(input())

def orders_func(product: str, quantity: int):
    result = 0
    if product == "coffee":
        price = 1.50
        result = quantity * price
    elif product == "coke":
        price = 1.40
        result = quantity * price
    elif product == "water":
        price = 1.00
        result = quantity * price
    elif product == "snacks":
        price = 2.00
        result = quantity * price
    return f"{result:.2f}"
print(orders_func(products, product_quantity))