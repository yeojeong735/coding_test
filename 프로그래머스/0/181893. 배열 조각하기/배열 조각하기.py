def solution(arr, query):
    
    i = 0
    for k in query:
        if i%2 == 0:
            arr = arr[:query[i]+1]
            i+=1
        else :
            arr = arr[query[i]:]
            i+=1
        
    
    
    answer = arr
    return answer