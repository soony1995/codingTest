# def solution(priorities, location):
#     answer = 0
#     # 중요도가 높을 수록 먼저
#     # 도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
#     # 중요도가 가장 높은 인덱스를 찾는다.
#     stack = []
#     maxValue = max(priorities)
#     index = 0
#     cnt = 0 
#     for i,v in enumerate(priorities):
#         if v == maxValue:
#             index = i
            
#     while cnt != index:
#         stack.append(priorities[cnt])
#         cnt += 1
#     list(priorities+stack)[index+location]
#     return 
def solution(p, l):
    answer = 0 
    maxV = max(p)
    while True:
        current = p.pop(0)
        if current == maxV:
            answer += 1
            if l == 0:
                break
            else:
                l -= 1
            maxV = max(p)
        else:
            p.append(current)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return answer
            
            
            
            
