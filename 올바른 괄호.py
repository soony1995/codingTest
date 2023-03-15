def solution(s):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # 맨앞에 ) 
    # 맨뒤에 (
    # (뒤에 ) 아니면 에러 -> "("와")"의 개수가 맞아야함.
    # count == 0의 리턴 값으로 boolean을 리턴해준다.
    # return bool
    count = 0
    for i in s:
        if i == "(":count += 1 
        elif i == ")":count -= 1
        if count < 0: return False
   
    return count == 0
