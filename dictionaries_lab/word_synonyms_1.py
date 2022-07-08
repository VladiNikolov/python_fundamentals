number = int(input())
synonyms = {}

for i in range(number):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
