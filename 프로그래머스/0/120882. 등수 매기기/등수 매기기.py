def solution(score):
    answer = []
    
    avergs = [ a + b for a,b in score]
    rank_base = sorted(avergs, reverse = True)
    return [ rank_base.index(v) + 1 for v in avergs]