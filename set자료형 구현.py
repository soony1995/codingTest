from collections import defaultdict

def main():     
    A = [1,1,2,3,3,4,4,5,6,7]
    dic = defaultdict(int)
    print(dic)
    for i in A:
        if dic[i]:
            continue
        dic[i] = 1 
    
    for v in dic:
        print(v)
    
if __name__ == "__main__":
    main()
