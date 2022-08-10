input_line = input().split()
input_line = list(map(int, input_line))
count_numbers = int(input())


while count_numbers > 0:
    temp = min(input_line)
    input_line.remove(temp)
    count_numbers -= 1
    
print(*input_line, sep=", ")
