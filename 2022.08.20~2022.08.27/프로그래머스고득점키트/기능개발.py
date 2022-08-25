def solution(progresses, speeds):
    
    stack = []
    answer = []
    for i in range(len(progresses)-1, -1, -1):
        a = 100 - progresses[i]
        if a % speeds[i] == 0:
            b = a // speeds[i]
        else:
            b = (a // speeds[i]) +1
            
        stack.append(b)
    count = 1
    x = stack.pop()
    while stack:
        if x >= stack[-1]:
            count += 1
            stack.pop()
        else:
            answer.append(count)
            x = stack.pop()
            count = 1
    answer.append(count)
        
    return answer

