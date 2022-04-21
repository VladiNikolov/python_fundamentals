# age = int(input())
#
# if age <= 14:
#     print("drink toddy")
# elif age <= 18:
#     print("drink coke")
# elif age <= 21:
#     print("drink beer")
# elif age > 21:
#     print("drink whisky")

age = int(input())
beverage = ""

if age <= 14:
    beverage = "drink toddy"
elif age <= 18:
    beverage = "drink coke"
elif age <= 21:
    beverage = "drink beer"
else:
    beverage = "drink whisky"
print(f"{beverage}")
