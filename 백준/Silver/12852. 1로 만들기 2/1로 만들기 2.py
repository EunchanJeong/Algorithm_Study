N = int(input())

dp = [0] * (N+1)
pre = [0] * (N+1)
dp[1] = 0
pre[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i-1

    if i%2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2] + 1
        pre[i] = i//2
    if i%3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3] + 1
        pre[i] = i//3

print(dp[N])

t = N
while t != 0:
    print(t, end=' ')
    t = pre[t]