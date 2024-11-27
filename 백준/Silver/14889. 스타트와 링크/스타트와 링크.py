import sys
input = sys.stdin.readline

N = int(input())
status = []
for _ in range(N):
    status.append(list(map(int, input().split())))

visited = [0] * N
result = int(1e9)

def dfs(count, player):
    global result

    if count == N // 2:
        team1 = 0
        team2 = 0

        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    team1 += status[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    team2 += status[i][j]
        result = min(result, abs(team1 - team2))
        return

    for i in range(player, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(count + 1, i + 1)
            visited[i] = 0

dfs(0, 0)
print(result)