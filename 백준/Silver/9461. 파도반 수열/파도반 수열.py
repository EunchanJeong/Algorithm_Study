import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)

    if N == 1:
        print(1)
    elif N == 2:
        print(1)
    elif N == 3:
        print(1)
    else:
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        
        for i in range(4, N+1):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[N])