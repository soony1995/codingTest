def solution(s):
    answer = []
    # 0 제거 => for 문
    # 출력값이 다시 입력값이 되는 로직 -> 함수로 만들어서 구현 -> 재귀 함수
    # 함수 에서 구현해야할 항목들:
    # 1. 마지막 return문에서 return 해줘야 할 값들 : 변환 카운트, 0카운트
    # 2. 아닐 경우, 문자열 s,변환 카운트, 0카운트
    # 3. answer 에 저장 후 return 

    ## 알게 된 사실 : 
    # 1. 파이썬은 다중리턴값이 있을 때에는 list를 쓸 경우 알아서 다 만들어준다. 
    # 2. 튜플도 된다.
    # 3. 이진법으로 변환 시에 bin(int값)[2:] 를 사용하면 된다. 왜냐면 0b가 붙기 떄문에.
    # 4. 재귀는 while문으로 대체 가능하다.
    # 5. 문자의 특정 문자의 개수를 세야 할 때에는 문자열.count("문자열")을 사용하자.
    # 6. 문자를 대체할 경우에는 문자열.replace("","")을 사용하자. 
    
    a = 0
    b = 0
    answer = removeZero(s,a,b)
    return answer

def removeZero(s,transCnt,zeroCnt):
    if s == "1":
        return transCnt,zeroCnt
    transCnt += 1
    b = ""
    for i in s:
        if i =="0":
            zeroCnt +=1
            continue
        b += i
    c = int(len(b))
    return removeZero(bin(c)[2:],transCnt,zeroCnt)
    
solution("110010101001")
"""
while True:
    if s == "1" :
        break;

    zeroCnt += s.count("0")
    s.replace("0","")
    s = bin(len(s))[2:]

    cnt += 1

answer = [cnt,zeroCnt]
return answer
"""
