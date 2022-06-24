secret_message = input().split()

strings_list = []
for word in secret_message:
    number = ""
    current_message = ""
    for character in word:
        if character.isdigit():
            number += character
        else:
            break
    word = word.replace(number, "")
    number = int(number)
    current_message += chr(number)
    if len(word) >= 2:
        word = word[-1] + word[1:-1] + word[0]
    current_message += word
    strings_list.append(current_message)
print(*strings_list)




