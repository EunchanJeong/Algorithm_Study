import copy

N, M = map(int, input().split())

graph = []
cctv = []
min_value = N * M

for i in range(N):
    t = list(map(int, input().split()))
    graph.append(t)
    
    for j in range(len(t)):
        if t[j] in [1, 2, 3, 4, 5]:
            cctv.append((t[j], i, j))


directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill(graph, d, x, y):
    for i in d:
        nx, ny = x, y
        
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 7
                
                
def dfs(depth, arr):
    global min_value
    
    if depth == len(cctv):
        count = 0
        
        for i in range(N):
            count += arr[i].count(0)
        
        min_value = min(min_value, count)
        return
    
    tmp = copy.deepcopy(arr)
    
    cctv_num, x, y = cctv[depth]
    
    for i in directions[cctv_num]:
        fill(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(arr)
        
dfs(0,graph)        
print(min_value)