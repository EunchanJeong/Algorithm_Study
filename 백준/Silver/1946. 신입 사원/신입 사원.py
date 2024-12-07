import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    p = []
    for _ in range(N):
        p.append(list(map(int, input().split())))
    p.sort()

    rank = p[0][1]
    count = 1
    for i in range(1, N):
       if rank > p[i][1]:
           count += 1
           rank = p[i][1]

    print(count)