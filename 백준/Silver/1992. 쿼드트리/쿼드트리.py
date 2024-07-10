N = int(input())
R = []
result = []

for _ in range(N):
    tmp = [int(i) for i in input()]
    R.append(tmp)

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if R[x][y] != R[i][j]:
                return False
    return True


def solve(x, y, z):
    if check(x, y, z):
        result.append(str(R[x][y]))
        return

    n = z//2
    result.append('(')
    for i in range(2):
        for j in range(2):
            solve(x+i*n, y+j*n, n)
    result.append(')')

solve(0, 0, N)
print(''.join(result))