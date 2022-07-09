my_dict = {}

input_string = "".join(i for i in input().split())
for symbol in input_string:
    if symbol not in my_dict:
        my_dict[symbol] = 0
    my_dict[symbol] += 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")

