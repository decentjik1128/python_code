import itertools

def solution(baseball):
    answer = 0

    numbers = list(itertools.permutations(range(1,10),3))
    numbers = list(map(lambda x : list(map(str, x)),numbers))


    print(numbers)
    return answer



baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
solution(baseball)
