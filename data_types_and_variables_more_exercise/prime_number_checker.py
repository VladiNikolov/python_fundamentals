number = int(input())

flag = False
i = 2
if number > 1:
    while i < number:

        if number % i == 0:
            flag = True
            break
        i += 1
if flag:
    print(f"False")
else:
    print(f"True")