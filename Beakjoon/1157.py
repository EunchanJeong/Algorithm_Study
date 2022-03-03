word = input()
word = word.upper()

alphabet = [0 for i in range(26)]

for ch in word:
    alphabet[ord(ch)-65] += 1

max_ch = max(alphabet)

index = alphabet.index(max_ch)

alphabet.pop(index)

if max_ch == max(alphabet):
    print("?")
else:
    print(chr(index+65))