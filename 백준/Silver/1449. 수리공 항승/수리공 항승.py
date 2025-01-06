import sys
input = sys.stdin.readline

N, L = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

result = 0
start = p[0]

for i in range(1, len(p)):
    if (p[i] - start) + 1 > L:
        result += 1
        start = p[i]
result += 1
print(result)