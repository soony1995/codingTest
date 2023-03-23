def solution(brown, yellow):
    # 브라운 격자의 크기 : 
    # 노란 격자의 가로 x 2 + 노란 격자의 세로x 2 + 4 = 24
    # 노란 격자의 약수를 구한다.
    a = []
    for i in range(1,yellow+1):
        if yellow % i == 0:
            a.append(i)
            
    while True:
        if (a[-1]*2 + a[0]*2 +4) == brown:
            break
        else:
            a.pop(0)
            a.pop()
            
    return [a[-1]+2,a[0]+2]
    # 위의 식에 만족하는 노란 격자의 가로 세로를 구한다.
    # 답은 노란 격자의 가로 + 2, 세로 격자 +2 
    
