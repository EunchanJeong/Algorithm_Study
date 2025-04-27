T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    earnings = list(map(int, input().split()))
    
    avg = sum(earnings)/N
    count = len([1 for e in earnings if e <= avg])
    
    print(f'#{test_case} {count}')