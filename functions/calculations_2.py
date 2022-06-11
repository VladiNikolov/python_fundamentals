def func_calculation(a, operator,b):
    if operator == "multiply":
        print(a * b)
    elif operator == "divide":
        print(int(a / b))
    elif operator == "add":
        print(a + b)
    elif operator == "subtract":
        print(a - b)

type_operator = input()
first_number = int(input())
second_number = int(input())
func_calculation(first_number, type_operator, second_number)