numbers = input().split(", ")


positive_list = []
negative_list = []
even_list = []
odd_list = []

for current_numbers in numbers:
    if int(current_numbers) >= 0:
        positive_list.append(current_numbers)
    if int(current_numbers) < 0:
        negative_list.append(current_numbers)
    if int(current_numbers) % 2 == 0:
        even_list.append(current_numbers)
    if int(current_numbers) % 2 != 0:
        odd_list.append(current_numbers)

print("Positive:" + " " + ", ".join(positive_list))
print("Negative:" + " " + ", ".join(negative_list))
print("Even:" + " " + ", ".join(even_list))
print("Odd:" + " " + ", ".join(odd_list))