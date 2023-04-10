def solution(array, commands):
    answer = []
    for start,end,pick in commands:
        tmp = []
        print(start,end,pick)
        tmp = array[start-1:end]
        tmp.sort()
        print(tmp)
        answer.append(tmp[pick-1])
    return answer
