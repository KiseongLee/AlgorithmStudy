import sys
input = sys.stdin.readline

n = int(input())

num = []
for i in range(1, n+1):
    num.append(i)

outs = []
for i in range(n):
    outs.append(int(input()))



def stack_():
    stack =[]
    result = []
    for out in outs:
    
        while True:
        
            if stack and stack[-1] > out:
                
                return print("NO")
        
            elif not stack or stack[-1] != out:
                stack.append(num.pop(0))
                result.append("+")
        
            elif stack and stack[-1] == out:
                stack.pop()
                result.append("-")
                break
    return print('\n'.join(result)) 

stack_()

        
