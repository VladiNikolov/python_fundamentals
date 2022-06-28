from math import floor

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
x_1 = floor(x_1)
y_1 = floor(y_1)
x_2 = floor(x_2)
y_2 = floor(y_2)
x_3 = floor(x_3)
y_3 = floor(y_3)
x_4 = floor(x_4)
y_4 = floor(y_4)

side_a_first_triangle = abs(x_1) + abs(x_2)
side_b_first_triangle = abs(y_1) + abs(y_2)
length_side_c_first_triangle = pow(side_a_first_triangle, 2) + pow(side_b_first_triangle, 2)

side_a_second_triangle = abs(x_3) + abs(x_4)
side_b_second_triangle = abs(y_3) + abs(y_4)
length_side_c_second_triangle = pow(side_a_second_triangle, 2) + pow(side_b_second_triangle, 2)

c_1 = pow(x_1, 2) + pow(y_1, 2)
c_2 = pow(x_2, 2) + pow(y_2, 2)
c_3 = pow(x_3, 2) + pow(y_3, 2)
c_4 = pow(x_4, 2) + pow(y_4, 2)

if length_side_c_first_triangle >= length_side_c_second_triangle:
    if c_1 <= c_2:
        print(f"({x_1}, {y_1})({x_2}, {y_2})")
    else:
        print(f"({x_2}, {y_2})({x_1}, {y_1})")
else:
    if c_3 <= c_4:
        print(f"({x_3}, {y_3})({x_4}, {y_4})")
    else:
        print(f"({x_4}, {y_4})({x_3}, {y_3})")
