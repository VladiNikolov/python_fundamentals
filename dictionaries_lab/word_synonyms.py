synonyms = {}

number = int(input())
for _ in range(number):
    word, synonym = input(), input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]
data = [f"{word} - {', '.join(synonym)}" for word, synonym in synonyms.items()]
print("\n".join(data))