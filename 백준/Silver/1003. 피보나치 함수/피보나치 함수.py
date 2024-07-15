T = int(input())

for _ in range(T):
    N = int(input())

    dp = [[0]*2 for _ in range(N+1)]

    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        dp[0][0] = 1
        dp[0][1] = 0

        dp[1][0] = 0
        dp[1][1] = 1

        dp[2][0] = 1
        dp[2][1] = 1


        for i in range(3, N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
        print(dp[N][0], dp[N][1])