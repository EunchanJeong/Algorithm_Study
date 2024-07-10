N = int(input())
count = [0, 0]
R = []

for _ in range(N):
    R.append(list(map(int, input().split())))

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if R[x][y] != R[i][j]:
                return False
    return True
    
def solve(x, y, z):
    if check(x, y, z):
        count[R[x][y]] += 1
        return
    
    n = z//2
    for i in range(2):
        for j in range(2):
            solve(x+(i*n), y+(j*n), n)

solve(0, 0, N)

for c in count:
    print(c)