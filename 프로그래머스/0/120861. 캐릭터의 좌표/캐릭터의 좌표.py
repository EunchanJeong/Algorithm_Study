def solution(keyinput, board):
    user = [0, 0]
    
    x_max = board[0]//2
    x_min = -(board[0]//2)
    y_max = board[1]//2
    y_min = -(board[1]//2)
    
    for key in keyinput:
        if key == 'up':
            y = user[1] + 1
            
            if y <= y_max:
                user[1] = y
        elif key == 'down':
            y = user[1] - 1
            
            if y >= y_min:
                user[1] = y
        elif key == 'left':
            x = user[0] - 1
            
            if x >= x_min:
                user[0] = x
        elif key == 'right':
            x = user[0] + 1
            
            if x <= x_max:
                user[0] = x
                
    return user