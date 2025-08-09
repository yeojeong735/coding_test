def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, _, result = q.split()
        x, y, result = int(x), int(y), int(result)
        if op == '+':
            if result == (x+y):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if result == (x-y):
                answer.append('O')
            else:
                answer.append('X')
    return answer
            