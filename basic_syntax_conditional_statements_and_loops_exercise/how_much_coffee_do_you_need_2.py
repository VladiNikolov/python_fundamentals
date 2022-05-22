command = input()

coffee_count = 0
while command != "END":
    if command == "dog":
        coffee_count += 1
    elif command == "cat":
        coffee_count += 1
    elif command == "coding":
        coffee_count += 1
    elif command == "movie":
        coffee_count += 1
    elif command == "DOG":
        coffee_count += 2
    elif command == "CAT":
        coffee_count += 2
    elif command == "CODING":
        coffee_count += 2
    elif command == "MOVIE":
        coffee_count += 2
    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)

