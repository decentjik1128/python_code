def solution(number):
    answer = ''
    a = list(map(str,number))
    a.sort(key = lambda x: x*3 ,reverse = True)

    answer = ''.join(a)

    if int(answer) == 0:
        answer ='0'

    return answer
