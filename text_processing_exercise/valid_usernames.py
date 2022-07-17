usernames = input().split(", ")

for username in usernames:
    username_is_valid = True
    if not 3 <= len(username) <= 16:
        username_is_valid = False
    for character in username:
        if not (character.isalnum() or character == "_" or character == "-"):
            username_is_valid = False
    if " " in username:
        username_is_valid = False
    if username_is_valid:
        print(username)

