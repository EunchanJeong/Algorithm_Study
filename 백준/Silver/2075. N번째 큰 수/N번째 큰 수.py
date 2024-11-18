import sys
import heapq
input = sys.stdin.readline

N = int(input())

hq = []
for _ in range(N):
    values = list(map(int, input().split()))
    if not hq:
        for v in values:
            heapq.heappush(hq, v)
    else:
        for v in values:
            if hq[0] < v:
                heapq.heappush(hq, v)
                heapq.heappop(hq)

print(hq[0])