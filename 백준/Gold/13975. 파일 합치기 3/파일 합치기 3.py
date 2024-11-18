import sys
import heapq
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    size = int(input())

    hq = []
    nums = list(map(int, input().split()))
    for n in nums:
        heapq.heappush(hq, n)

    result = 0
    while len(hq) > 1:
        n1 = heapq.heappop(hq)
        n2 = heapq.heappop(hq)
        result += n1 + n2
        heapq.heappush(hq, n1+n2)

    print(result)