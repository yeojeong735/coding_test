from collections import Counter;
def solution(a, b, c, d):
    nums = [a,b,c,d]
    cnt = Counter(nums)
    answer = 0
    
    if(4 in cnt.values()):
        answer = 1111 * a
    elif(3 in cnt.values()):
        p = next(k for k,v in cnt.items() if v == 3)
        q = next(k for k,v in cnt.items() if v == 1)
        answer = (10 * p + q) ** 2
    elif(list(cnt.values()).count(2) == 2):
        pair = [k for k, v in cnt.items() if v == 2]
        p, q = pair[0], pair[1]
        answer = (p + q) * abs(p - q)
    elif(2 in cnt.values()):
        p, q = [k for k, v in cnt.items() if v == 1]
        answer = p * q
    else:
        answer = min(nums)
    
    
    
    return answer