def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution3(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

def solution4(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer

def solution5(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        result.append(sorted(array[i-1:j])[k-1])
    return result

def solution6(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

print(solution2(array,commands))
