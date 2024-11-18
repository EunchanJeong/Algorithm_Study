import sys
import heapq
input = sys.stdin.readline

N = int(input())
left_hq = []
right_hq = []

idx = 0
for i in range(N):
    num = int(input())

    if len(left_hq) == len(right_hq):
        heapq.heappush(left_hq, -num)
    else:
        heapq.heappush(right_hq, num)
    if right_hq and (-left_hq[0]) > right_hq[0]:
        left = heapq.heappop(left_hq)
        right = heapq.heappop(right_hq)
        heapq.heappush(right_hq, -left)
        heapq.heappush(left_hq, -right)
    print(-left_hq[0])