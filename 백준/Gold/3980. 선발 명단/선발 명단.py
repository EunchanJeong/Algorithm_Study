import sys
input = sys.stdin.readline

def dfs(num, score):
    global max_score

    if num == 11:
        max_score = max(max_score, score)
        return

    for i in range(11):
        if visited[i] == 0 and players[num][i] != 0:
            visited[i] = 1
            positions[num] = i
            dfs(num+1, score + players[num][i])
            positions[num] = -1
            visited[i] = 0

T = int(input())
for _ in range(T):
    players = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    positions = [-1] * 11
    visited = [0] * 11

    dfs(0, 0)

    print(max_score)