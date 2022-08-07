import re
pattern = r"\|(?P<boss_name>[A-Z]{4,})\|:#(?P<title>[A-Za-z]+ [A-Za-z]+)#"
number_of_bosses = int(input())

for _ in range(number_of_bosses):
    line = input()

    regex = re.match(pattern, line)

    if not regex:
        print("Access denied!")
    else:
        extract_boss = regex.group("boss_name")
        extract_title = regex.group("title")

        print(f"{regex.group(1)}, The {regex.group(2)}")
        print(f">> Strength: {len(extract_boss)}")
        print(f">> Armor: {len(extract_title)}")

