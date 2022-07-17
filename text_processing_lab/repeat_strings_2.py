words = input().split(" ")

result = [word * len(word) for word in words]
print("".join(result))
# print(*result, sep = "")