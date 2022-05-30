a = int(input())
b = int(input())

b, a = b, a
print("Before:")
print(f"a = {a}")
print(f"b = {b}")
print("After:")
print(f"a = {b}")
print(f"b = {a}")