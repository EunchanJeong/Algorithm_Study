import sys
input = sys.stdin.readline

words = []

for _ in range(5):
    tmp = input().strip()
    words.append(tmp)

max_len = max(len(word) for word in words)

result = ""
for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            result += words[j][i]

print(result)