from collections import deque

def bfs(node):
    q = deque()

    visited[node] = 1
    q.append(node)

    while q:
        n = q.popleft()

        if n in graph:
            for g in graph[n]:
                if visited[g] == 0:
                    visited[g] = visited[n] + 1
                    q.append(g)

for test_case in range(1, 11):
    length, start = map(int, input().split())

    inputs = list(map(int, input().split()))

    graph = {}
    visited = {}

    for i in set(inputs):
        visited[i] = 0

    for i in range(0, len(inputs)-1, 2):
        if inputs[i] in graph:
            graph[inputs[i]].append(inputs[i+1])
        else:
            graph[inputs[i]] = [inputs[i+1]]

    bfs(start)

    result = [k for k, v in visited.items() if max(visited.values()) == v]

    print(f"#{test_case} {max(result)}")
