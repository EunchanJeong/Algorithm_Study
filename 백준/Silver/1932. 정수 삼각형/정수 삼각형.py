import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dp = [[0]*N for _ in range(N)]

dp[0][0] = graph[0][0]
for i in range(1, N):
    for j in range(len(graph[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + graph[i][j], dp[i-1][j] + graph[i][j])

print(max(dp[N-1]))