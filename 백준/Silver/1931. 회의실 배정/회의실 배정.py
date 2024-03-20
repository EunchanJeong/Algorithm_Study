import sys
input = sys.stdin.readline

N = int(input())

meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append([s, e])

meetings.sort(key = lambda x: [x[1], x[0]])

time = 0
count = 0

for meeting in meetings:
    if meeting[0] < time:
        continue
    time = meeting[1]
    count += 1

print(count)