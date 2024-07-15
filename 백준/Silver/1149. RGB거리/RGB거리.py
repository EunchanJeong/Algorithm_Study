N = int(input())

colors = []
dp = [[0]*3 for _ in range(N+1)]

colors.append([-1, -1, -1])
for _ in range(N):
    tmp = list(map(int, input().split()))
    colors.append(tmp)

dp[1][0] = colors[1][0]
dp[1][1] = colors[1][1]
dp[1][2] = colors[1][2]

for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + colors[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + colors[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + colors[i][2]

print(min(dp[N]))