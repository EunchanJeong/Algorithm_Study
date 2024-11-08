T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    graph = []
    answer = 0
    for _ in range(N):
        t = list(map(int, input().split()))
        graph.append(t)
        
    for x in range(N):
        for y in range(N):
            if 0 <= x + M - 1 < N and 0 <= y + M - 1 < N:
                count = 0
                for a in range(x, x+M):
                    count += sum(graph[a][y:y+M])
                if count > answer:
                    answer = count
    print("#" + str(i) + " " + str(answer))