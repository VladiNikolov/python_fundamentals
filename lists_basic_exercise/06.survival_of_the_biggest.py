input_integer = input().split()
input_integer = [int(i) for i in input_integer]
numbers_to_remove = int(input())

for element in range(numbers_to_remove):
    temp = min(input_integer)
    input_integer.remove(temp)
print(", ".join(map(str, input_integer)))