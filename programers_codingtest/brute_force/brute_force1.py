def solution(answers):
    answer = []
    count = [0, 0, 0]
    check1 = [1, 2, 3, 4, 5]
    check2 = [2, 1, 2, 3, 2, 4, 2, 5]
    check3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == check1[i % 5]:
            count[0] +=1
        if answers[i] == check2[i % 8]:
            count[1] +=1
        if answers[i] == check3[i % 10]:
            count[2] +=1

    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)

    return answer

answers = [1, 2, 3, 4, 5]
print(solution(answers))
