country = input().split(", ")
capital = input().split(", ")
result = {key: value for key, value in zip(country, capital)}
for key, value in result.items():
    print(f"{key} -> {value}")
