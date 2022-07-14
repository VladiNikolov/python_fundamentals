while True:
    command = input()
    reversed_text = ""
    if command == "end":
        break
    else:
        for word in reversed(command):
            reversed_text += word
        print(command + " = " + reversed_text)
