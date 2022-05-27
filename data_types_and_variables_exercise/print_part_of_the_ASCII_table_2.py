start = int(input())
end = int(input())
current_char = ""
for character in range(start, end + 1):
    current_char = chr(character) + chr(32)
    print(current_char, end= "")