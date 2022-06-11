def func_calculates(first_num, operator, second_num):
    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return int(first_num / second_num)
    elif operator == "add":
        return first_num + second_num
    elif operator == "subtract":
        return first_num - second_num

input_operator = input()
first_number = int(input())
second_number = int(input())
print(func_calculates(first_number, input_operator, second_number))