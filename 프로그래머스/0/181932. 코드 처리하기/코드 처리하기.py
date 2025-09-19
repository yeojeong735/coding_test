def solution(code):
    
    mode = 0
    ret = ''
    
    for idx, x in enumerate(code):
        if mode == 0:
            if x != "1" and idx%2 == 0:
                ret += x
            elif x == '1':
                mode = 1
        elif mode == 1:
            if x != "1" and idx%2 == 1:
                ret += x
            elif x == "1":
                mode = 0
    
    
    if ret == '':
        return "EMPTY"
    else :
        return ret