
"""
문제 설명
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
"""

## 숫자 비교 이기 때문에 string -> int로 바꾸는작업이 필요하다.
## string 인데 구분자가 있으므로 split을 사용했음. => string array 
## string array -> int array 
## sort를 이용해서 처음과 끝을 추출 
## str(array[0]) + " " + str(array[-1])

## 알게된 점:
#  1. array / 원시타입 정도만 신경을 쓰고 있으면 된다.
#  2. list에 min(list) max(list) 을 통해 찾을 수 있다는 것도 알게됨.

def solution(s):
    answer = ''
    num_list = list(map(int, s.split(' ')))
    min_num = min(num_list)
    max_num = max(num_list)
    answer = str(min_num) + " " + str(max_num)
    return answer

def solution(s):
    answer = ''
    numbers = sorted([int(i) for i in s.split(" ")])
    return str(numbers[0])+ str(numbers[-1])
    
a = ["1 2 3 4","-1 -2 -3 -4","-1 -1"]
for i in a:
    print(solution(i))

    