T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    
    h = arr[0] + arr[2]
    m = arr[1] + arr[3]
    
    if m >= 60:
        h += m//60
        m = m%60
    if h > 12:
        h = h%12
        if h == 0:
            h = 12
    print(f'#{test_case} {h} {m}')