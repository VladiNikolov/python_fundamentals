input_strings = input().split()
word = input()

palindromes = []
for current_word in input_strings:
    if current_word == current_word[::-1]:
        palindromes.append(current_word)

print(palindromes)
print(f"Found palindrome {palindromes.count(word)} times")