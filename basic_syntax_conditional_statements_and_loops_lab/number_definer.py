# number = float(input())
#
# if number == 0:
#     print("zero")
# elif number > 0:
#     if number < 1:
#         print("small positive")
#     elif number > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# else:
#     if number > -1:
#         print("small negative")
#     elif number < -1000000:
#         print("large negative")
#     else:
#         print("negative")

number = float(input())

if number == 0:
    print("zero")
elif 0 < number < 1:
    print("small positive")
elif 1 < number < 1000000:
    print("positive")
elif number > 1000000:
    print("large positive")
if -1 < number < 0:
    print("small negative")
elif -1 > number > -1000000:
    print("negative")
elif number < - 1000000:
    print("large negative")
