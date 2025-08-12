def solution(names):
    answer = []
    i = 0
    while i < len(names):
        if i%5 == 0:
            answer.append(names[i])
        i += 1
        
    return answer