N = int(input())
P = list(map(int, input().split()))

P.sort()

count = 0

for idx, value in enumerate(P):
    if idx != 0:
        count += sum(P[:idx]) + value
    else:
        count += value

print(count)