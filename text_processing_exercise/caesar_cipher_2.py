result = [ord(i) + 3 for i in input()]
for element in result:
    print("".join(chr(element)), end="")