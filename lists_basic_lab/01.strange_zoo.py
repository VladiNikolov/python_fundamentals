first_input = input()
second_input = input()
third_input = input()

meerkat = [first_input, second_input, third_input]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)