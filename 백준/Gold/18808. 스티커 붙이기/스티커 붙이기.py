N, M, K = list(map(int, input().split()))
graph = [[0]*M for _ in range(N)]

def checking(graph, sticker, i, j):
    for s_y in range(len(sticker)):
        for s_x in range(len(sticker[0])):
            if graph[i+s_y][j+s_x] + sticker[s_y][s_x] > 1:
                return False
    return True

def attach(graph, sticker, i, j):
    for s_y in range(len(sticker)):
        for s_x in range(len(sticker[0])):
            graph[i+s_y][j+s_x] += sticker[s_y][s_x]
    return

def rotate(arr):
    n = len(arr)
    m = len(arr[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

for _ in range(K):
    y, x = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(y)]
    
    check = False
    count = 0
    
    while count < 4:
        if check:
            break
        
        if len(sticker) > N or len(sticker[0]) > M:
            sticker = rotate(sticker)
            count += 1
            continue
        
        for i in range(N - len(sticker) + 1):
            if check:
                break
            for j in range(M - len(sticker[0]) + 1):
                if checking(graph, sticker, i, j):
                    attach(graph, sticker, i, j)
                    check = True
                    break
        sticker = rotate(sticker)
        count += 1

result = sum(sum(row) for row in graph)
print(result)