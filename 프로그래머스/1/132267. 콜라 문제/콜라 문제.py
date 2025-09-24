def solution(a, b, n):
    
    answer = 0
    
    while n >= a:
        new_cok = (n // a) * b
        
        empty_cok = n % a
        
        answer += new_cok
        
        n = empty_cok + new_cok
    return answer