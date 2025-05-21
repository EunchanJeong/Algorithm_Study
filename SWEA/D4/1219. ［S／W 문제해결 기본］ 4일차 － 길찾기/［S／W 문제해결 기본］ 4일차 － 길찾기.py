def dfs(node):
    if node == 99:
        return 1

    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            if dfs(n) == 1:
                return 1
            visited[n] = False

    return 0

for _ in range(0, 10):
    test_case, road = map(int, input().split())
    nums = list(map(int, input().split()))

    graph = [[] for _ in range(100)]
    visited = [False for _ in range(100)]

    for i in range(0, len(nums)-1, 2):
        graph[nums[i]].append(nums[i+1])

    result = dfs(0)

    print(f"#{test_case} {result}")
