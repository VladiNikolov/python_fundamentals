import math

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_1 = math.floor(x_1)
y_1 = math.floor(y_1)
x_2 = math.floor(x_2)
y_2 = math.floor(y_2)

c_1 = x_1**2 + y_1**2
c_2 = x_2**2 + y_2**2
if c_1 == c_2:
    print(f"({x_1}, {y_1})")
elif c_1 < c_2:
    print(f"({x_1}, {y_1})")
elif c_1 > c_2:
    print(f"({x_2}, {y_2})")


