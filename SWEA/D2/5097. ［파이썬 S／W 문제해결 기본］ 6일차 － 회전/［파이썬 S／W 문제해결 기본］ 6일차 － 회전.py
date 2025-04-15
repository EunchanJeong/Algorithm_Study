from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = deque(list(map(int, input().split())))
    
    for _ in range(M):
        t = nums.popleft()
        nums.append(t)
        
    print(f'#{test_case} {nums[0]}')
    
    
    
