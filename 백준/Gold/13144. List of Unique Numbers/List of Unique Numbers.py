N = int(input())
L = list(map(int, input().split()))

result = 0
start, end = 0, 0
seq = [False] * 1000001

while start < N and end < N:
    if not seq[L[end]]:
        seq[L[end]] = True
        end += 1
        result += end - start
    else:
        seq[L[start]] = False
        start += 1
print(result)