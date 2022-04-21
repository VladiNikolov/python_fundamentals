a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# import sys
# max_size = -sys.maxsize
# for number in range(3):
#     current_number = int(input())
#     if current_number > max_size:
#         max_size = current_number
# print(max_size)