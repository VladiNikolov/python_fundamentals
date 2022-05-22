command = input()

count_coffee = 0
while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or \
            command == "movie" or command == "CODING" or command == "DOG" or\
            command == "CAT" or command == "MOVIE":
        if command.islower():
            count_coffee += 1
        else:
            command.isupper()
            count_coffee += 2
    command = input()
if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)