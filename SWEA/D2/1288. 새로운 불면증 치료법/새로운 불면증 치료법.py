T = int(input())

for test_case in range(1, T+1):
    L = []
    
    N = int(input())
    i = 1
    while True:
        L += list(str(N*i))
        L = list(set(L))
        if len(L) == 10:
            break
        i += 1
    print(f'#{test_case} {N*i}')        