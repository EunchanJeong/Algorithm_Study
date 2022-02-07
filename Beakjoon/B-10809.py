alphabet = [-1 for _ in range(26)]

word = input()

for i in range(len(word)):
    index = ord(word[i])-97

    if (alphabet[index] == -1):
        alphabet[index] = i

for i in range(len(alphabet)):
    print(alphabet[i], "", end="")