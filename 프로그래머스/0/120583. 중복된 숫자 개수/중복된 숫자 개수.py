from collections import Counter;
def solution(array, n):
    cnt = Counter(array)
    
    answer = cnt[n]
    return answer