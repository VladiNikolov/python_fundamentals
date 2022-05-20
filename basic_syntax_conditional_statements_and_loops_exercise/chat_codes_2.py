number = int(input())

greetings = ""
i = 0

while i < number:
    current_number = int(input())
    if current_number == 88:
        greetings = "Hello"
    elif current_number == 86:
        greetings = "How are you?"
    elif current_number == 87 or current_number < 86:
        greetings = "GREAT!"
    elif current_number > 88:
        greetings = "Bye."
    i += 1
    print(greetings)