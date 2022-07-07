input_data = input().split()

product_dict = {}

for i in range(0, len(input_data), 2):
    product_dict[input_data[i]] = int(input_data[i + 1])

print(product_dict)
