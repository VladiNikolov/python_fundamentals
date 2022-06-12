def validation(some_string):
    password_is_valid = True
    if len(some_string) < 6 or len(some_string) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    if not some_string.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    digits_counter = 0
    for character in some_string:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    return password_is_valid

some_password = input()
is_valid = validation(some_password)
if is_valid:
    print("Password is valid")