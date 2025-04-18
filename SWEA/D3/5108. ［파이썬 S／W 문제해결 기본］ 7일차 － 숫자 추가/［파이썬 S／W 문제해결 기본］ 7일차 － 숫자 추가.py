T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    l = list(map(int, input().split()))
    
    for _ in range(M):
        idx, value = map(int, input().split())
        l.insert(idx, value)
    print(f'#{test_case} {l[L]}')
    