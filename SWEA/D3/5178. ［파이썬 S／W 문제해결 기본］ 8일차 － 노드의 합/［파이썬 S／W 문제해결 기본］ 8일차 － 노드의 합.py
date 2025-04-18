T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    
    tree = [0 for _ in range(N+1)]
    
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
        
    for i in range(N, 0, -1):
        if i // 2 > 0:
            tree[i//2] += tree[i]
    print(f'#{test_case} {tree[L]}')