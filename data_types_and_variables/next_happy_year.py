year = int(input())

is_year_happy = False
while not is_year_happy:
    year = year + 1
    str_year = str(year)
    set_year = set()
    for i in range(len(str_year)):
        set_year.add(str_year[i])

    is_year_happy = len(str_year) == len(set_year)
print(year)

