# number = int(input())
# num = str(number)
#
# m = sorted(num, reverse = True)
# for d, digit in enumerate(m):
#     print(digit, end="")
#
number = int(input())
num = str(number)
m = sorted(num, reverse = True)
for i, digit in enumerate(m):
    print(digit, end="")

