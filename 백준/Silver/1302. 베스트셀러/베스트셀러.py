import sys
input = sys.stdin.readline

N = int(input())
words = {}

for _ in range(N):
    word = input().strip()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

max_value = max(words.values())
max_keys = [key for key, value in words.items() if value == max_value]

print(min(max_keys))