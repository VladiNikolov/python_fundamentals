country = input().split(", ")
capital = input().split(", ")

for index in range(len(country)):
    print(f"{country[index]} -> {capital[index]}")