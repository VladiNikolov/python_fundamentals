# tail = input()
# body = input()
# head = input()
#
# meerkat = [head, body, tail]
#
# print(meerkat)
#
#-----------------------------------
#
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# print(meerkat)
#
#-------------------------------------------
#
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# temp = meerkat[0]
# meerkat[0] = meerkat[2]
# meerkat[2] = temp
#
# print(meerkat)
#
#----------------------------------------
#
# meerkat = list()
# for i in range(3):
#     current_string = input()
#     meerkat.append(current_string)
# meerkat.reverse()
#
# print(meerkat)
#
#--------------------------------------------
#
meerkat = []

meerkat.append(input())
meerkat.append(input())
meerkat.append(input())
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)
