meerkat = []

meerkat.append(input())
meerkat.append(input())
meerkat.append(input())

temp = meerkat[0]
meerkat[0] = meerkat[2]
meerkat[2] = temp

print(meerkat)