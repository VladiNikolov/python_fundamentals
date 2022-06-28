from math import floor

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_1 = floor(x_1)
y_1 = floor(y_1)
x_2 = floor(x_2)
y_2 = floor(y_2)

c_1 = pow(x_1, 2) + pow(y_1, 2)
c_2 = pow(x_2, 2) + pow(y_2, 2)
if c_1 == c_2:
    print(f"({x_1}, {y_1})")
elif c_1 < c_2:
    print(f"({x_1}, {y_1})")
elif c_1 > c_2:
    print(f"({x_2}, {y_2})")