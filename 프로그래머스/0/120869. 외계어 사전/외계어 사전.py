
def solution(spell, dic):
    answer = 0
    
    for k in dic:
        if sorted(k) == sorted(spell):
            answer = 1
            break
        else:
            answer = 2
            
    return answer