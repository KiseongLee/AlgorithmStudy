import sys
input = sys.stdin.readline

k = int(input())
stack = []

for i in range(k):

    num = int(input())
    
    if num != 0:
        stack.append(num)
    
    else:
        stack.pop()
    

sum = 0
for i in stack:
    sum += i

print(sum)