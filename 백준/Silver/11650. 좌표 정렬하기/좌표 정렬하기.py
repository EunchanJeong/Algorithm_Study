import sys
input = sys.stdin.readline

N = int(input())
xy = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    xy.append(tmp)

xy.sort()

for i in xy:
    print(i[0], i[1])