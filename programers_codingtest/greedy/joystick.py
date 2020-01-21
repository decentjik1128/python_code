def solution(name):
    answer = 0
    up_down_result = []

    for i in range(len(name)):
        tmp = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        up_down_result.append(tmp)
        answer += tmp
    
    index = 0

    for i in range(len(up_down_result) - up_down_result.count(0)):
        left = 1
        right = 1

        up_down_result[index] = 0

        if sum(up_down_result) == 0:
            break

        while up_down_result[index - left ] == 0:
            left += 1

        while up_down_result[index + right] == 0:
            right += 1
        
        if left < right:
            index -= left
            answer += left
        else:
            index += right
            answer += right

    return answer

print(solution('JEROEN'))
print(solution('JAN'))
print(solution('AAABAAA'))
print(solution('BBAABB'))