def solution(n):
    # n+1 크기의 리스트를 만들고 True로 초기화합니다.
    # 0과 1은 소수가 아니므로 False로 표시합니다.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # 2부터 숫자를 확인하며 배수들을 소수가 아니라고 표시합니다.
    # n의 제곱근까지만 확인하면 충분합니다.
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i의 배수들을 False로 만듭니다.
            # i*i부터 시작하는 이유는 그 이전 배수들은 이미 처리되었기 때문입니다.
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # is_prime 리스트에서 True인 값들의 개수를 셉니다.
    answer = sum(is_prime)
    
    return answer