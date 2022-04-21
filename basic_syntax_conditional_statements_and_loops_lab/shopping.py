budget = int(input())
command = input()
while command != "End":
    price_product = int(command)
    budget = budget - price_product
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")