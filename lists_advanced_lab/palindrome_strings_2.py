words = input().split()
search_word = input()

palindrome_list = [el for el in words if el == el[::-1]]
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(search_word)} times")