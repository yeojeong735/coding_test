def solution(num, total):
    # 1. 시작 숫자(x) 구하기
    sum_of_consecutive = (num - 1) * num // 2
    start_num = (total - sum_of_consecutive) // num
    
    # 2. 연속된 숫자 리스트 만들기
    answer = [start_num + i for i in range(num)]
    
    return answer