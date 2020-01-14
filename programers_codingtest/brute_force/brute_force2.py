import itertools,math

def solution(numbers):

    answer = 0
    answer_set = []
    noanswer_set = []

    for i in range(len(numbers)):
        answer_set += list(map(int,(map(''.join, itertools.permutations(numbers, i+1)))))

    answer_set = set(answer_set)

    answer = len(answer_set & set(prime_list(max(answer_set)+1)))

    return answer

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

print(solution('17'))