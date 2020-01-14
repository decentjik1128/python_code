def solution1(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

def solution2(numbers):
    nums = [str(n) for n in numbers]
    longest = max([len(n) for n in nums], default=0)
    nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
    return str(int(''.join(nums)))

def solution3(numbers):
    answer = ''
    numbers = sorted(numbers, reverse=True, key=lambda  x: (str(x)*4).ljust(4))
    for i in numbers:
        answer += str(i)
    if answer[0] == '0':    #모두 0인 경우 -> 테스트11
        return '0'
    return answer

def solution4(numbers):
    from functools import cmp_to_key
    def sortFunction(n1,n2):
        return int(str(n1)+str(n2))-int(str(n2)+str(n1))
    return str(int("".join([str(n) for n in sorted(numbers, key=cmp_to_key(sortFunction), reverse=True)])))

from functools import cmp_to_key

def solution5(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers = sorted(numbers, key=cmp_to_key(lambda a, b: -1 if a+b >= b+a else 1))
    answer = ''.join(numbers)

    return str(int(answer))
