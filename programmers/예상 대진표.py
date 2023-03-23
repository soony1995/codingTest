def solution(n,a,b):
    answer = 0
    #1,2 -> 1 
    #3,4 -> 2 
    #5,6 -> 3 
    #7,8 -> 4
    
    #4명씩 한 그룹으로 묶자.! 2의 n 지수승이 힌트
    
    #2명 이하 일 경우에는 무조건 1번
    
    #a 와 b를 4로 나눈 나머지가 1,2 또는 3,4일 때 stop
    
    #4명 이상일 경우
    #4로 나눈 나머지가 1,2 일 경우 1 
    #4로 나눈 나머지가 3,4 일 경우 2 
    
    min_num = min(a,b)
    max_num = max(a,b)
    if n == 2 :
        return 1 
    while True:
        n = n // 4 
        if min_num%4 ==1 and max_num%4 ==2 or min_num%4 ==3 and max_num%4 == 0:
            return answer
            break;
            
        if min_num %4 == 1 or min_num %4 == 2 :
            if min_num // 4 <= 1:
                n = 1
            else:
                n = 2
            min_num = 1 * n
            print("11")
        elif min_num %4 == 3 or min_num %4 == 0 :
            if min_num // 4 <= 1:
                n = 1
            else:
                n = 2
            min_num = 2 * n 
            print("22")
            
            
        if max_num %4 == 1 or max_num %4 == 2 :
            if max_num // 4 <= 1:
                n = 1
            else:
                n = 2
            max_num = 1 * n
            print("33")
        elif max_num %4 == 3 or max_num %4 == 0 :
            if max_num // 4 <= 1:
                n = 1
            else:
                n = 2
            print(int(max_num // 4))
            max_num = 2 * n
            print("44")

        print(min_num,max_num)
        break
        answer += 1
    # a가 홀수 번 일때,
        #다음 번에도 홀 수 
    # a가 짝수 번 일때, 
    #1번 그룹
    # N명 참가 -> 짝수.! 
    # 짝수 /2 => 그룹의 수가 나옴. -> 
    # 첫라운드에서 번호는 두번째라운드가 되면 바뀔 수 있다.
    # 4 -> 2 -> 1 
    # 7 -> 4 -> 2 
    # 만난다? => 사실상 1,2 3,4 5,6 은 같은 그룹이라고 보면 된다. 
    # a와 b가 홀수인지 짝수인지 중요. -> 같은 그룹이 되었을 때 연산할 수 있기 때문에.
    # 짝수 그룹은 
            
    # return 몇번째 라운드에서 만나는지? 

    return answer
    
    *************** 정답 *************
    1. 힌트 : 2의 지수승이라는 것.
    2. 1 2 3 4 5 6 7 8 
    
    1//2 = 0  1%2 = 1
    2//2 = 1  2%2 = 0
    3//2 = 1  3%2 = 1 
    4//2 = 2  4%2 = 0 
    이런식으로 몫 + 나머지가 같은 것 끼리 한 그룹이 형성된다.
    
    2 로 나눈다 => 2명씩 한 그룹으로 짝지운ㄷ
