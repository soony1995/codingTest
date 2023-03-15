def solution(A,B):
    answer = 0

    # 두 array 비교 
    # 단순 비교 for 문 2개 
        # 문제, 이미 사용된 것을 제외해야함.
    # 큰거 X 작은거 
    # 내림 차순 정렬, 오름 차순 정렬 
    # 하나씩 zip을 이용해 곱하기 
    A.sort()
    B.sort(reverse = True)
    for x,y in zip(A,B):
        answer += x*y
    return answer