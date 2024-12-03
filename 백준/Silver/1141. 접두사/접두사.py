import sys
input = sys.stdin.readline

N = int(input())

words = [input().strip() for _ in range(N)]
words.sort()

count = 0
for i in range(len(words)):
    tmp = words[i+1:]

    for t in tmp:
        if t.find(words[i]) == 0:
            count += 1
            break

print(len(words) - count)