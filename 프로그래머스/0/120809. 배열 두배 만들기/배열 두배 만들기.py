def solution(numbers):
    n = 0
    for k in numbers:
        numbers[n] = numbers[n] * 2
        n += 1
        
    answer = numbers
    return answer