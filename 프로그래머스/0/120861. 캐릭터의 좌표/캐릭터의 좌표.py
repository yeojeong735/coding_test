def solution(keyinput, board):
    
    location = [0,0]
    
    limit_x = board[0] // 2
    limit_y = board[1] // 2
    
    for k in keyinput:
        if k == 'left':
            if location[0] == -limit_x:
                continue
            else:
                location[0] = location[0] - 1
        elif k == 'right':
            if location[0] == limit_x:
                continue
            else:
                location[0] = location[0] + 1
        elif k == 'up':
            if location[1] == limit_y:
                continue
            else:
                location[1] = location[1] + 1
        elif k == 'down':
            if location[1] == -limit_y:
                continue
            else:
                location[1] = location[1] - 1
    
    return location