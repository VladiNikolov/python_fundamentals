command = input()

count_coffee = 0
while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        count_coffee += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        count_coffee += 2
    command = input()
if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)



