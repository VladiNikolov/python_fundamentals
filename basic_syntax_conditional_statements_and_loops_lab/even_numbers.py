number = int(input())
for i in range(number):
    current_number = int(input())
    if current_number % 2 == 1:
        print(f"{current_number} is odd!")
        break
else:
    print("All numbers are even.")

