def solution(a, b):
    answer = 0
    
    string1 = str(a) + str(b)
    num1 = int(string1)
    
    string2 = str(b) + str(a)
    num2 = int(string2)
    
    if num1 > num2:
        answer = num1
    else:
        answer = num2
    return answer