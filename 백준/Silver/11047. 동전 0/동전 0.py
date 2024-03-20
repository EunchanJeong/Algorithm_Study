import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0
for coin in coins:
    if coin <= K:
        t = K//coin
        K -= coin*t
        count += t

    if K == 0:
        break
print(count)