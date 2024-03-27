def solution(board):
    answer = 0

    for y, value in enumerate(board):
        for x, v in enumerate(value):
            if v == 1:
                if (x != 0):
                    if board[y][x-1] == 0:
                        board[y][x-1] = 2
                    if (y != 0) and board[y-1][x-1] == 0:
                        board[y-1][x-1] = 2

                    if (y < len(board)-1) and board[y+1][x-1] == 0:
                        board[y+1][x-1] = 2

                if (x < len(value)-1): 
                    if board[y][x+1] == 0:
                        board[y][x+1] = 2

                    if (y != 0) and board[y-1][x+1] == 0:
                        board[y-1][x+1] = 2

                    if (y < len(board)-1) and board[y+1][x+1] == 0:
                        board[y+1][x+1] = 2

                if (y != 0) and board[y-1][x] == 0:
                    board[y-1][x] = 2
                if (y < len(board)-1) and board[y+1][x] == 0:
                    board[y+1][x] = 2
    answer = 0
    for i in board:
        answer += i.count(0)

    return answer