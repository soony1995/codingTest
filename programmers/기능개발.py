def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

// 처음 인자가 100이 되는 시점에 그 이후 인덱스를 검사해 만약에 100이 된게 잇다면 전부 cnt를 늘리고 pop을 할 생각이였음.
// 이렇게 생각하니 복잡해 로직을 짜는데 어려움이 생김.
// 그냥 간단하게 하나씩 하면 되는걸..
