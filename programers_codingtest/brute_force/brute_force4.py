def solution(brown, red)

    for i in range(1, red + 1):
        if red % i ==0: # 사각형 구조 만들기 가능
            if (i+2) * (red // i + 2) - red == brown:
                return [ max(i+2,red // i + 2), min(i+2,red // i + 2)]
