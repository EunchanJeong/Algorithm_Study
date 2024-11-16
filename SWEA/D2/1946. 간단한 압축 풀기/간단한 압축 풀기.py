T = int(input())

for t in range(1, T+1):
    N = int(input())

    s = ''
    for _ in range(N):
        c, size = input().split()
        s += c*int(size)

    print(f'#{t}')
    for i in range(0, len(s), 10):
        print(s[i:i+10])