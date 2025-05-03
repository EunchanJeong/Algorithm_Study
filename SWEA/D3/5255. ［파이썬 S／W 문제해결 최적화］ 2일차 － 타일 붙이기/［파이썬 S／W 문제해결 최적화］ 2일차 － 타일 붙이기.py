T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    dp = [-1] * (num+1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6
    
    for i in range(4, num+1):
        dp[i] = dp[i-1] + dp[i-2] * 2 + dp[i-3]
    print(f"#{test_case} {dp[num]}")
    
