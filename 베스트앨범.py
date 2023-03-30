def solution(genres, plays):
    answer = []
    
    1. genre의 순서
        genre 별 plays 값을 비교해야함.
    2. plays의 순서
        genre 내에서 play의 수가 높은 2개의 인덱스를 리턴해야함.
    
    딕셔너리의 key 값으로 잡을 수 있는 항목들:
        generes, plays,index가 있지만, 
        리턴해줘야 하는 값이 index 이고, 비교해야할 값들이 value 값이기 때문에
        key 값으로 generes를 가진다.
        
    dic1 = {} 
    dic2 = {} 

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
