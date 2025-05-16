T = 10

for test_case in range(1, T + 1):
    N = int(input())
    
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    board = list(map(list, zip(*board)))
    
    count = 0
    for b in board:
        flag = False
        for t in b:
            if t == 1:
                flag = True
            if flag and t == 2:
                count += 1
                flag = False
                
    print(f"#{test_case} {count}")
