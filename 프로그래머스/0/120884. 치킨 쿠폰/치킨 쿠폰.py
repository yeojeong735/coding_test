def solution(chicken):
    answer = 0
    while chicken >= 10:
        servise = chicken // 10
        answer += servise
        chicken = chicken % 10 + servise
    return answer