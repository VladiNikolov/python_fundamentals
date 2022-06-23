numbers = input().split(", ")

print("Positive:" + " " + ", ".join([current_numbers for current_numbers in numbers if int(current_numbers) >= 0]))
print("Negative:" + " " + ", ".join([current_numbers for current_numbers in numbers if int(current_numbers) < 0]))
print("Even:" + " " + ", ".join([current_numbers for current_numbers in numbers if int(current_numbers) % 2 == 0]))
print("Odd:" + " " + ", ".join([current_numbers for current_numbers in numbers if int(current_numbers) % 2 != 0]))