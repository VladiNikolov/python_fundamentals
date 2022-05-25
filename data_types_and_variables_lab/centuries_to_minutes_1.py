input_centuries = int(input())

year = input_centuries * 100
days = int(year * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{input_centuries} centuries = {year} years = {days} days = {hours} hours = {minutes} minutes")