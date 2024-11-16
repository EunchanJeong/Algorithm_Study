T = int(input())

for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    
    total_A = P * W
    total_B = 0
    
    if W > R:
        total_B = Q + (W-R)*S
    else:
        total_B = Q
    
    answer = min(total_A, total_B)
    print(f'#{test_case} {answer}')
    