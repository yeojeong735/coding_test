def solution(n):
    num = 0   # 유효한 숫자 개수
    i = 0     # 현재 숫자
    
    while num < n:
        i += 1
        if i % 3 == 0 or "3" in str(i):
            continue
        num += 1
    
    return i