def solution(cards1, cards2, goal):
    answer = "Yes"
    
    for g in goal:
        if len(cards1) > 0 and cards1[0] == g :
            del cards1[0]
        elif len(cards2) > 0 and cards2[0] == g :
            del cards2[0]
        else :
            answer = "No"
    
    
        
    return answer