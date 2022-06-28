def printTribRec(number):
    if (number == 0 or number == 1 or number == 2):
        return 1
    elif (number == 3):
        return 2
    else:
        return (printTribRec(number - 1) +
                printTribRec(number - 2) +
                printTribRec(number - 3))


def printTrib(number):
    for i in range(1, number + 1):
        print(printTribRec(i), "", end="")


number = int(input())
printTrib(number)
