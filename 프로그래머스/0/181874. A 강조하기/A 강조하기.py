def solution(myString):
    answer = ''
    
    for ch in myString:
        if ch == 'a':
            answer += ('A')
        elif ch != 'A' and ch.isupper():
            answer += (ch.lower())
        else :
            answer += ch
    return answer