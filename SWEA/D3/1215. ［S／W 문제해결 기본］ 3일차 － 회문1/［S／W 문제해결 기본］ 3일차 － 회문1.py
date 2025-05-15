for test_case in range(1, 11):
    str_len = int(input())
    
    board = []
    for _ in range(8):
        board.append(list(input().strip()))
    
    count = 0
    for b in board:
        for i in range(0, len(b) - str_len + 1):
            if b[i:i+str_len] == b[i:i+str_len][::-1]:
                count += 1

    board = list(map(list, zip(*board)))
    for b in board:
        for i in range(0, len(b) - str_len + 1):
            if b[i:i+str_len] == b[i:i+str_len][::-1]:
                count += 1
    
    print(f"#{test_case} {count}")