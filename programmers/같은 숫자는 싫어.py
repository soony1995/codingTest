def solution(arr):
    answer = []
    # 연속적으로 나타나는 숫자 제거 
    # 기본적으로 stack을 사용할 수 있다. 
    stack = []
    i = 0
    while i < len(arr):
        if len(stack) == 0:
            stack.append(arr[i])
        else:    
            if stack[-1] != arr[i]:
                stack.append(arr[i])
        i += 1
    return stack

  
  
 다른 사람 풀이
 result = []
    for c in s:
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result
