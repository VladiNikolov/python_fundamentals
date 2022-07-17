def valid_len(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def character_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True

def other_symbol(username):
    if " " in username:
        return False
    return True

usernames = input().split(", ")
for username in usernames:
    if valid_len(username) and character_are_valid(username) and other_symbol(username):
        print(username)