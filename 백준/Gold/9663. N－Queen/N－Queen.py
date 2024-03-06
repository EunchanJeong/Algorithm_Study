import sys
input = sys.stdin.readline

N = int(input())

map = [[0]*N for _ in range(N)]

issued1 = [0 for _ in range(N)]
issued2 = [0 for _ in range((2*N)-1)]
issued3 = [0 for _ in range((2*N)-1)]
count = 0

def backtracking(k):
    global count
    if k == N:
        count += 1
        return

    for i in range(N):
        if not(issued1[i] or issued2[k+i] or issued3[k-i+N-1]):
            issued1[i] = issued2[k+i] = issued3[k-i+N-1] = 1
            backtracking(k+1)
            issued1[i] = issued2[k+i] = issued3[k-i+N-1] = 0


backtracking(0)
print(count)