from collections import Counter
def solution(array):
    cnt = Counter(array)
    max_freq = max(cnt.values())
    answer = 0
    
    modes = [k for k,v in cnt.items() if v == max_freq]
    
    if len(modes)>1:
        return -1
    else:
        return modes[0]
