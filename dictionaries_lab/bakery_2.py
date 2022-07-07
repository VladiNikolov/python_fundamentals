input_elements = input().split()

bakery_dict = {input_elements[i]: int(input_elements[i + 1]) for i in range(0, len(input_elements), 2)}

print(bakery_dict)
