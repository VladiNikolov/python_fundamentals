cards = input().split()
shuffle = int(input())

length = len(cards)
mid = int(length / 2)

for i in range(0, shuffle):
    list = []
    for p in range(0, mid):
        list.append(cards[p])
        list.append(cards[mid])
        mid += 1
    cards = list
    mid = int(length / 2)

print(list)

