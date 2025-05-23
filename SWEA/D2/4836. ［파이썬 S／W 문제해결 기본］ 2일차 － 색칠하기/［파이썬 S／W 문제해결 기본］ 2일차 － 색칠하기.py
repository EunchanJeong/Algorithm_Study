T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    graph = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        inputs = list(map(int, input().split()))

        for x in range(inputs[0], inputs[2] + 1):
            for y in range(inputs[1], inputs[3] + 1):
                if graph[x][y] != inputs[4]:
                    graph[x][y] += inputs[4]

    count = 0
    for g in graph:
        for i in g:
            if i > 2:
                count += 1

    print(f"#{test_case} {count}")