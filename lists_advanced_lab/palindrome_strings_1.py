def palindrome_filter(word):
    if word == word[::-1]:
        return word

input_strings = input().split(" ")
searched_word = input()
palindrome_list = [word for word in input_strings if palindrome_filter(word)]

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(searched_word)} times")