T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    graph = []
    for _ in range(N):
        row = list(map(int, input().split()))
        graph.append(row)

    r_g = list(zip(*graph))

    answer = 0
    for i in range(N):
        count1 = 0
        count2 = 0
        for j in range(N):
            if graph[i][j] == 0:
                if count1 == K:
                    answer += 1
                count1 = 0
            else:
                count1 += 1

            if r_g[i][j] == 0:
                if count2 == K:
                    answer += 1
                count2 = 0
            else:
                count2 += 1

        if count1 == K:
            answer += 1
        if count2 == K:
            answer += 1
    print(f'#{t} {answer}')
