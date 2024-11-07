S = input()
words = [S[i:] for i in range(len(S))]
words.sort()

for w in words:
    print(w)