import re
pattern = r"(?P<name>[A-Za-z0-9!@#$?]+)=(?P<len>\d+)<<(?P<code>(.*?)+)$"

command = input()

while command != "Last note":

    regex = re.match(pattern, command)

    if not regex:
        print("Nothing found!")
    else:
        extract_name = regex.group("name")
        extract_len = int(regex.group("len"))
        extract_code = regex.group("code")

        new_string = ""
        if extract_len != len(extract_code):
            print("Nothing found!")
        else:
            for i in range(len(extract_name)):
                if extract_name[i].isalnum():
                    new_string += extract_name[i]

            print(f"Coordinates found! {new_string} -> {extract_code}")

    command = input()