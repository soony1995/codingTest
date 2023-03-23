## 나의 풀이 
def solution(n):
    answer = 0
    return recursive(n,answer)

def recursive(n,answer):
        if n == 0:
            answer += 0
            return answer
        if n == 1 or n == 2 :
            answer += 1
            return answer
        # if n < 2 :
            #return n
        return  (recursive(n-2,answer) + recursive(n-1,answer) ) % 1234567

## 정석 풀이
def solution(n):
    fib = [0, 1, 1]
    for i in range(3, n + 1):
        fib.append((fib[i-2] + fib[i-1]) % 1234567)
    
    return print(fib[-1])

solution(5)

## 이 문제의 경우 재귀함수로 풀 경우 timeout이 나게된다. 
## 하지만 아래의 풀이처럼 기존의 값을 저장해 놓는 다면 해결됨.
## list의 index와 값을 매핑하여 푸는 문제.
