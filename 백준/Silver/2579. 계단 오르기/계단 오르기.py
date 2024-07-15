N = int(input())

S = [-1]
for i in range(N):
    S.append(int(input()))

if N == 1:
    print(S[N])
else:
    dp = [[0]*3 for _ in range(N+1)]         

    dp[1][1] = S[1]
    dp[1][2] = 0

    dp[2][1] = S[2]
    dp[2][2] = S[1] + S[2]

    for i in range(3, N+1):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + S[i]
        dp[i][2] = dp[i-1][1] + S[i]

    print(max(dp[N][1], dp[N][2]))