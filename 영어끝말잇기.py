def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return print([(i%n)+1, (i//n)+1])
    else:
        return print([0,0])
    
solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])

# 이 문제를 풀지 못헀던 이유 .
# 1. 값 두개를 리스트로 묶어주는 문법을 몰랐음. => 그냥 [value,value] 식으로 하면 되는건데..
# 2. 리스트에 있는 인접한 두 개의 값을 비교하는 방법을 몰랐음.
# -> while 과 for문을 이용해 어렵게 접근했음.
# 3. 나머지 연산자와 몫 연사자 사용하는 법에 대해서 익숙하지 않았음.
# -> 0으로 떨어질 때 +1을 안해줌.
