num = int(input())
trib = [1, 1, 2, 4]

for i in range(3, num):
    trib.append(trib[i] + trib[i - 1] + trib[i - 2])
final_trib = []
for i in range(num):
    final_trib.append(trib[i])

print(*final_trib, sep=" ")