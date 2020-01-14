def solution(citations):
    answer = 0

    for i in range(max(citations)+1):
        if i <= len(list(filter(lambda x: x >= i, citations))):
             answer = i

    return answer


citations = [3,0,6,1,5]
solution(citations)
