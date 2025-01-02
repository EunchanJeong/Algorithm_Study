from collections import deque
import sys
input = sys.stdin.readline

N, d, k, c=map(int, input().split())

sushi_list=[]
for _ in range(N):
    sushi_list.append(int(sys.stdin.readline().strip()))

max_sushi=0
cnt=0
eat=deque()

for i in range(k-1):
    eat.append(sushi_list[i])

for j in range(N):
    eat.append(sushi_list[(j + k - 1) % N])
    cnt=0
    if c not in eat: #쿠폰 번호가 없을 경우
        cnt=1
    if max_sushi<len(set(eat))+cnt:
        max_sushi=len(set(eat))+cnt
    eat.popleft()


print(max_sushi)