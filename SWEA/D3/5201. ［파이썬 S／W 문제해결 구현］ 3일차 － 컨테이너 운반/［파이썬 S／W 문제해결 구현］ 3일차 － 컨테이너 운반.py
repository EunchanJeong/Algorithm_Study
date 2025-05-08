T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    containers = list(map(int, input().split()))
    containers.sort(reverse=True)
    
    trucks =  list(map(int, input().split()))
    trucks.sort(reverse=True)
	
    result = 0
    for t in trucks:
        for idx, weight in enumerate(containers):
            if weight <= t:
                result += weight
                containers.pop(idx)
                break
 
    print(f"#{test_case} {result}")
                