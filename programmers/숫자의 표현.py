def solution(n):
    answer = 0
    # 15를 만들어야 하니 15에서 입력값을 빼는 형태로 함.
    # 성공하는 케이스 실패하는 케이스 전부 존재한다.
    # 15이하의 자연수로 채워야한다.
    # 같은 개수의 식은 나오지 못한다. -> 연속한 자연수 이기 떄문에.
    for i in range(1,n+1):
        a = 0
        for j in range(i,n+1):
            a += j 
            if a > n:
                break
            if a == n:
                answer += 1
                break
    return answer