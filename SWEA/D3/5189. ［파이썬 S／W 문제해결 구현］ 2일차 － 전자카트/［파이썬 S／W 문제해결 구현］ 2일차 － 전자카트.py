def dfs(graph, idx, count, result, visited, size, answer):
    if count == size - 1:
        answer.append(result + graph[idx][0])
        return

    for i in range(size):
        if visited[i]:
            continue
        visited[i] = True
        dfs(graph, i, count + 1, result + graph[idx][i], visited, size, answer)
        visited[i] = False


T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    graph = [list(map(int, input().split())) for _ in range(size)]
    visited = [False] * size
    answer = []

    visited[0] = True
    dfs(graph, 0, 0, 0, visited, size, answer)

    print(f"#{test_case} {min(answer)}")