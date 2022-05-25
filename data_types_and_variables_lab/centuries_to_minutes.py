import math

centuries = int(input())
year = centuries * 100
days = year * 365.2422
hours = math.floor(days) * 24
minutes = hours * 60
print(f"{centuries} centuries = {year} years = {math.floor(days)} days = {hours} hours = {minutes} minutes")
