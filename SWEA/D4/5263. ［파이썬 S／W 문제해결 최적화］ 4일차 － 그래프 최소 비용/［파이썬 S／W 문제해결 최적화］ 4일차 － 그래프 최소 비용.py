T = int(input())
INF = int(1e9)

for test_case in range(1, T + 1):
    N = int(input())
    dist = []

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if i != j and row[j] == 0:
                row[j] = INF 
        dist.append(row)
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    max_min_cost = -INF
    for i in range(N):
        for j in range(N):
            if i != j and dist[i][j] != INF:
                max_min_cost = max(max_min_cost, dist[i][j])

    print(f"#{test_case} {max_min_cost}")