from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())

pq = PriorityQueue()
for _ in range(N):
    n = int(input())

    if n == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    else:
        pq.put((abs(n), n))
