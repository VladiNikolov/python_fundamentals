people = input().split()
k = int(input())
josephus_permutation = []

index = 0
while len(people) > 0:
    index = (index + k - 1) % len(people)
    josephus_permutation.append(people.pop(index))

print(f"[" + ",".join(map(str, josephus_permutation)) + "]")
