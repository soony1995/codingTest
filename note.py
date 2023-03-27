def solution():
    letter = input()
    n = int(input())
    stack = []
    for _ in range(n):
        command = input().split()
        if command[0] == "L":
            if len(letter) != 0:
                stack.append(letter[-1])
                letter = letter[:-1]
        elif  command[0] == "R": 
            if len(stack) != 0:
                letter.append(stack[-1])
                stack.pop()
        else: # p일 떄 
            stack.insert(0command[1])
            print("stack",stack)
    print([letter]+stack)
            
    
    return

solution()