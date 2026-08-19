word = input() + ' запретил букву'
alphabet = []

for i in range(len(word)):
    if word[i].isalnum() and word[i] not in alphabet:
        alphabet.append(word[i])

alphabet.sort()

for i in range(len(alphabet)):
    print(f"{word} {alphabet[i]}")
    word = word.replace(alphabet[i], '')
    word = " ".join(word.split())