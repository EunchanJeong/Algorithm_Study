T = int(input())

for r in range(1, T+1):
    print(f'#{r}')
    n = int(input())
    pascal = [[0]*n for _ in range(n)]
    pascal[0][0] = 1
    print(pascal[0][0])
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            if pascal[i][j] != 0:
                print(pascal[i][j], end=' ')
        print()