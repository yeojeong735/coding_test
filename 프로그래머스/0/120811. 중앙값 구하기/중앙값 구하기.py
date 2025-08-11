def solution(array):
    array.sort()
    
    num = len(array) // 2
    
    answer = array[num]
    return answer