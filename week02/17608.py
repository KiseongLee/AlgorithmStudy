import sys
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    
    a = int(input())
    stack.append(a)

max_value = stack[-1]
count = 1
for i in range(n-1, -1, -1):
    
    if stack[i] > max_value:
        count += 1
        max_value = stack[i]

print(count)
        
    

        