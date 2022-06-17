vowels = ['a', 'o', 'u', 'e', 'i']
input_line = input()
result = [letter for letter in input_line if letter.lower() not in vowels]
print(*result, sep="")