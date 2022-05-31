key = int(input())
number_of_string = int(input())

for i in range(number_of_string):
    current_string = input()
    new_string = ord(current_string) + key
    print(chr(new_string), end= "")