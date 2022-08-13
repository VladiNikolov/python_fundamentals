country = input().split(", ")
capital = input().split(", ")

result_dict = dict(zip(country, capital))
for element in result_dict:
    print(f"{element} -> {result_dict[element]}")