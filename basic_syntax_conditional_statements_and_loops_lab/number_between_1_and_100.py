# number = float(input())
#
# while number < 1 or number > 100:
#     number = float(input())
# print(f"The number {number} is between 1 and 100")

# import sys
# for i in range(sys.maxsize):
#     number = float(input())
#     if 1 <= number <= 100:
#         break
# print(f"The number {number} is between 1 and 100")

import sys

for i in range(sys.maxsize):
    number = float(input())
    if number < 1 or number > 100:
        continue
    else:
        print(f"The number {number} is between 1 and 100")