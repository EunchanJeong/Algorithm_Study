import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
first = 1
last = max(lines)
res=0
while(first<=last):
    mid = (first+last)//2
    target = 0
    for line in lines:
        target += line//mid

    if target>=n:
        first = mid+1
        res=mid

    else:
        last = mid-1

print(res)