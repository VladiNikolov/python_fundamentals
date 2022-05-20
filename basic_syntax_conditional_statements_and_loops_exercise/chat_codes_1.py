number = int(input())

greetings = ""

for _ in range(number):
    current_number = int(input())
    if current_number == 88:
        greetings = "Hello"
    elif current_number == 86:
        greetings = "How are you?"
    elif current_number == 87 or current_number < 86:
        greetings = "GREAT!"
    elif current_number > 88:
        greetings = "Bye."
    print(greetings)
