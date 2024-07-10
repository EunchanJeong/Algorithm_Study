N = int(input())

R = []

for _ in range(N):
    row = list(map(int, input().split()))
    R.append(row)

count = [0, 0, 0]

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if R[x][y] != R[i][j]:
                return False
    return True

def solve(x, y, z):
    if check(x, y, z):
        count[R[x][y] + 1] += 1
        return

    n = z // 3
    for i in range(3):
        for j in range(3):
            solve(x + (i * n), y + (j * n), n)

solve(0, 0, N)

for c in count:
    print(c)