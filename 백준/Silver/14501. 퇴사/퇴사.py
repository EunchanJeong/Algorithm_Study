import sys
input = sys.stdin.readline

N = int(input())

counsel = []
for _ in range(N):
    counsel.append(list(map(int, input().split())))

dp = [0 for i in range(N+1)]

for i in range(N):
    # print(i)
    for j in range(i+counsel[i][0], N+1):
        if dp[j] < dp[i] + counsel[i][1]:
            dp[j] = dp[i] + counsel[i][1]

print(max(dp))