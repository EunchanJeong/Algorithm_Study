import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
M = int(input())

result = 0
start, end = 1, max(L)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for l in L:
        if l > mid:
            total += mid
        else:
            total += l
    if total <= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)