def solution(n):
    std = n
    answer = n+1
    # n 의 다음 큰숫자
    # str(n).count("1") = str(bin(a)).count("1")
    # 만족하는 a 중 가장 작은 수 
    while True:
        if str(bin(n)[2:]).count("1") == str(bin(answer)[2:]).count("1"): ## 굳이 str로 바꾸지 않아도 바이너리로 바꿀 수 있다.
            break
        answer += 1
    return answer
  
 
