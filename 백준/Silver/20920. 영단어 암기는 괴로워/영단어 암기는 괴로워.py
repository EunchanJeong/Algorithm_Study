import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_count = {}

for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

result = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in result:
    print(word)