my_dict = {}
key_dict = []
value_dict = []
input_string = "".join(i for i in input().split())
for symbol in input_string:
    if symbol not in my_dict:
        my_dict[symbol] = 0
    my_dict[symbol] += 1

for key in my_dict.keys():
    key_dict.append(key)

for value in my_dict.values():
    value_dict.append(value)

for (k, v) in zip(key_dict, value_dict):
    print(f"{k} -> {v}")

