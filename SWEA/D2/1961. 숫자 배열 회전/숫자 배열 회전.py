T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    graph_90 = list(zip(*graph[::-1]))
    graph_180 = list(zip(*graph_90[::-1]))
    graph_270 = list(zip(*graph_180[::-1]))

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(map(str, graph_90[i])), end=' ')
        print(''.join(map(str, graph_180[i])), end=' ')
        print(''.join(map(str, graph_270[i])), end=' ')
        print()
