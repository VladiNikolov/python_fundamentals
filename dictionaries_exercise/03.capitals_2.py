country = input().split(", ")
capital = input().split(", ")

final_dict = {}
for element in country:
    if element not in final_dict:
        final_dict[element] = capital[0]
        capital.pop(0)
for key, value in final_dict.items():
    print(f"{key} -> {value}")
