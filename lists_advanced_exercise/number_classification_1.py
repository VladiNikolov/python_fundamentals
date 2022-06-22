numbers = input().split(", ")

positive_list = []
negative_list = []
even_list = []
odd_list = []

for current_numbers in numbers:
    positive_list = [current_numbers for current_numbers in numbers if int(current_numbers) >= 0]
    negative_list = [current_numbers for current_numbers in numbers if int(current_numbers) < 0]
    even_list = [current_numbers for current_numbers in numbers if int(current_numbers) % 2 == 0]
    odd_list = [current_numbers for current_numbers in numbers if int(current_numbers) % 2 != 0]

print("Positive:" + " " + ", ".join(positive_list))
print("Negative:" + " " + ", ".join(negative_list))
print("Even:" + " " + ", ".join(even_list))
print("Odd:" + " " + ", ".join(odd_list))