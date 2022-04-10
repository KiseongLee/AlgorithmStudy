import sys
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    
    a = input().strip()
    
    if " " in a:
        b = a.split(" ")
        stack.append(b[1])
        
    if a == "top":
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)   
    
    if a == "size":
        if stack:
            print(len(stack))
        else:
            print(0)
    
    if a == "empty":
        if stack:
            print(0)
        else:
            print(1)
    
    if a == "pop":
        if stack:
            print(stack[len(stack)-1])
            stack.pop()
        else:
            print(-1)
    
