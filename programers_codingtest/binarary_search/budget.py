def solution(budgets, M):
    answer = 0
    left =0
    right = max(budgets)

    if sum(budgets) <= M:
        return right
   
    while right >= left:
        mid = (left + right ) // 2
        sum_budget = 0
       
        for i in budgets:
            if mid < i:
                i = mid
            sum_budget += i
                
        if sum_budget < M:
            left = mid + 1
            answer = mid                           
        elif sum_budget > M:
            right = mid - 1           
        else:
            return mid 
        print(mid, sum_budget)

    return answer     


print(solution([120, 110, 140, 150], 485))