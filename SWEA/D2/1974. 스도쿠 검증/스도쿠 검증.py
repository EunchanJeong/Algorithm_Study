T = int(input())

for t in range(1, T+1):
    graph = []
    for _ in range(9):
        row = list(map(int, input().split()))
        graph.append(row)
    answer = 1
    a = list(zip(*graph))
    for i in range(9):
        if len(list(set(graph[i]))) != 9 or len(list(set(a[i]))) != 9:
            answer = 0
            break

    if answer == 1:
        for i in range(3):
            for j in range(3):
                count = [0] * 10
                for k in range(3):
                    for l in range(3):
                        count[graph[i*3+k][j*3+l]] += 1
                for c in range(1, 10):
                    if count[c] != 1:
                        answer = 0
                        break

    print(f'#{t} {answer}')