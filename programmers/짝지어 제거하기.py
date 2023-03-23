def solution(s):
    answer = -1
    # 찾고 제거 해야함.
    # for 앞의 문자 == 뒤의 문자 
    # 둘다 제거 (전의 문자와 현재 문자에 대한 정보를 가지고 있어야함.) -> for문 부적격.-> stack  사용
    # 출력값을 다시 입력값으로 사용해야함. -> 재귀함수 or while 을 사용해야함. 반복문도 사용해야 하기 때문에 while문으로 처리. -> 시간 초과 
    i = 0
    while True:
        if s =="":
            answer = 1
            break; 
        if i+2 > len(s):
            answer = 0
            break;    
        for j in range(i+1,i+2):
            print(i,j)
            if s[i] == s[j]:
                s = s[:i] + s[i+1:]
                s = s[:i] + s[i+1:]
                i = 0
            else:
                i += 1
    # 다시 재조합. 
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return print(answer)

def solution1():
    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i :
                stack.pop()
            else:
                stack.append(i)
                
    if not stack:
        return 1
    else :
        return 0
    
solution1()
