N = int(input())

dp = [0 for _ in range(N+1)]

if N == 1:
    print(1)
else:
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = (dp[i-1]+dp[i-2])

    print(dp[N]%10007)