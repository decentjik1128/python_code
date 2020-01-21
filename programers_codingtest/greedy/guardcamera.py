def solution(routes):
    answer = 0
    last_camera = 30000
    
    routes = sorted(routes)

    for i in reversed(routes):
        if last_camera > i[1]:
            answer += 1
            last_camera = i[0]

    return answer


print(solution([[-20,15], [-14,-5], [-18, -13], [-5, -3]]))