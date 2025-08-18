def solution(n, control):
    answer = 0
    
    for k in control:
        if k == 'w':
            n += 1
        elif k == 's':
            n -= 1
        elif k == 'd':
            n += 10
        else :
            n-= 10
      
    answer = n
    return answer