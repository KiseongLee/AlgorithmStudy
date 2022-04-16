import sys
input = sys.stdin.readline

target = input().strip()
bomb = input().strip()
stack= []

for i in range(len(target)):
    
    stack.append(target[i])
    
    if stack[-1] == bomb[-1]:
        if "".join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
        
                

if not stack:
    print("FRULA")
else:
    print("".join(stack))
                