def main():     
    A = [1,2,3,4,5,6] # 주어진 숫자
    N = 4 # 뽑을 수자의 개수
    visited = [0]* len(A) # A의 자리수 체크하는 리스트
    result = [0]* N # 결과가 담길 리스트
    final = []
    
    def permutation(level):
        if level == N: # 재귀는 종료조건을 항상 먼저 써야한다.                   
            final.append(result.copy())
            return 
            
        for i in range(len(A)):
            if visited[i]: continue
            
            visited[i] = 1
            result[level] = A[i]
            permutation(level+1)
            visited[i] = 0
    
    permutation(0)
    print(final)
    
if __name__ == "__main__":
    main()
