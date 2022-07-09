country = input().split(", ")
capital = input().split(", ")

country_dict = {country[index] : capital[index] for index in range(len(capital))}
for key, value in country_dict.items():

    print(f"{key} -> {value}")
