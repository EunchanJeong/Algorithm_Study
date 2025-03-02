import sys
input = sys.stdin.readline

N = int(input())
segments = [list(map(int, input().split())) for _ in range(N)]

segments.sort()

result = 0

start, end = segments[0]

for s, e in segments[1:]:
    if s <= end:  
        end = max(end, e) 
    else: 
        result += end - start  
        start, end = s, e

result += end - start

print(result)