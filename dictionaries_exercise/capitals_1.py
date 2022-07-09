country = input().split(", ")
capital = input().split(", ")

country_dict = dict(zip(country, capital))
for key, value in country_dict.items():
    print(f"{key} -> {value}")