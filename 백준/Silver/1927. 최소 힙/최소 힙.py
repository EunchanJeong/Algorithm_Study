import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            answer = heapq.heappop(hq)
            print(answer)
    else:
        heapq.heappush(hq, num)