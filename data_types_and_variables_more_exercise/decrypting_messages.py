key = int(input())
number_of_letters = int(input())

for i in range(number_of_letters):
    current_letter = input()
    current_number = ord(current_letter)
    new_number = current_number + key
    print(f"{chr(new_number)}", end="")
