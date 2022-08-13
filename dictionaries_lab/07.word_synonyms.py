number = int(input())

synonyms_dict = {}
for i in range(number):
    key_word = input()
    value_synonym = input()
    if key_word not in synonyms_dict:
        synonyms_dict[key_word] = []
        synonyms_dict[key_word].append(value_synonym)
    else:
        synonyms_dict[key_word].append(value_synonym)
for keys, values in synonyms_dict.items():
    print(f"{keys} - {', '.join(values)}")