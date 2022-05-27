start_input = int(input())
end_input = int(input())

while start_input <= end_input:
    current_char = chr(start_input)
    start_input += 1
    print(f"{current_char}", end= " ")