my_budget = int(input())
command = input()
condition = False
while command != "End":
    product_price = int(command)
    if my_budget >= product_price:
        my_budget -= product_price
    else:
        print("You went in overdraft!")
        condition = True
        break

    command = input()
if not condition:
    print("You bought everything needed.")
