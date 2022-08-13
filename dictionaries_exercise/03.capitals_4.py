country = input().split(", ")
capital = input().split(", ")

final_dict = {}
for index in range(len(country)):
    if country[index] not in final_dict:
        final_dict[country[index]] = capital[index]
for keys, value in final_dict.items():
    print(f"{keys} -> {value}")

