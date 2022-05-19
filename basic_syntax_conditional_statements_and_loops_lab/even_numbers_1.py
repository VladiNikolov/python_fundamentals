number = int(input())
is_all_number_even = False
for num in range(number):
    current_number = int(input())
    if current_number % 2 == 0:
        is_all_number_even = True
        continue
    else:
        is_all_number_even = False
        print(f"{current_number} is odd!" )
        break
if is_all_number_even:
    print("All numbers are even.")