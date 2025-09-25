def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for request in d:
        if budget >= request:
            budget -= request
            answer += 1
        else:
            break
    
    
    return answer