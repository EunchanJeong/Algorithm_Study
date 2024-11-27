from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())

check = []
for _ in range(N):
    check.append(list(map(int, input().split())))

distance = [0]
for i in range(N-1):
    d = abs(check[i][0]-check[i+1][0]) + abs(check[i][1]-check[i+1][1])
    distance.append(d)

distance_total = sum(distance)

result = []
for i in range(1, N-1):
    d = distance_total - (distance[i] + distance[i + 1]) + abs(check[i + 1][0] - check[i - 1][0]) + abs(check[i + 1][1] - check[i - 1][1])
    result.append(d)

print(min(result))