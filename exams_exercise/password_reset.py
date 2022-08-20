def password_reset():
    data= input()

    while True:

        command = input().split()

        if command[0] == "Done":
            print(f"Your password is: {data}")
            break

        elif command[0] == "TakeOdd":
            data = "".join([data[i] for i in range(len(data)) if i % 2 != 0])
            print(data)

        elif command[0] == "Cut":
            index = int(command[1])
            length = int(command[2])
            data = "".join([data[i] for i in range(len(data)) if i < index or i >= index + length])
            print(data)

        elif command[0] == "Substitute":
            substring = command[1]
            substitute = command[2]
            if substring in data:
                data = data.replace(substring, substitute)
                print(data)
            else:
                print("Nothing to replace!")
password_reset()