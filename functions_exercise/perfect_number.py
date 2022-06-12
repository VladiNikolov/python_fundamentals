def is_perfect(number):
    sum = 0
    for devisor in range(1, number):
        if number % devisor == 0:
            sum += devisor
    if number == sum:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))