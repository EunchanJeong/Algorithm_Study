from itertools import combinations

N, M = map(int, input().split())

house = []
chicken = []
for i in range(N):
    data = list(map(int, input().split()))
    
    for j in range(N):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))
            
result = N * M * len(house)
for comb in combinations(chicken, M):
    dist_total = 0
    for a, b in house:
        dist = N * M * len(house)
        
        for i in range(M):
            dist = min(dist, abs(a-comb[i][0]) + abs(b-comb[i][1]))
        dist_total += dist
    
    result = min(result, dist_total)

print(result)