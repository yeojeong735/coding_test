def solution(picture, k):
    answer = []
    
    for row in picture:
        enlarged = ''.join(ch * k for ch in row)
        for _ in range(k):
            answer.append(enlarged)
        
        
        
    return answer