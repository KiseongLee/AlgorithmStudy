
'''
import sys
input = sys.stdin.readline

n = int(input())

stack =[]


for i in range(n):
    sum = 0
    a = input().rstrip()
    
    a = list(a)
    
    for j in a:
        if j == "(":
            
            sum += 1
            
        
        if j == ")":
            
            sum -= 1
        
        if sum < 0 :
            
            break
        
        
    if sum == 0:
        print("YES")
    else:
        print("NO")

'''


t = int(input())

for i in range(t):
    stack = []
    a = input()
    for j in a :
        if j == '(':
            stack.append(j)
    
        elif j == ')':
            if stack:
                stack.pop()
      
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
    

  
    

