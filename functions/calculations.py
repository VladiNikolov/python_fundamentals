def calculation_func(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result

operator = input()
first_number = int(input())
second_number = int(input())
print(calculation_func(first_number, second_number, operator))