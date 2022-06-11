input_number = input().split(", ")

for current_element in input_number:
    if current_element == current_element[::-1]:
        print("True")
    else:
        print("False")

