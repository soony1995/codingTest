def solution(progresses, speeds):

    stack = []
    
    k = 1
    
    while k<len(speeds):
        for i in speeds:
            print(i,k)
            progresses[k] += i * k 
            print(progresses[k])
        
        k += 1
        
    return 
