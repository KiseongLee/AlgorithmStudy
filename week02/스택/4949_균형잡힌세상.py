

stack = []
out = []
while True:
    
    a = input()
    
    if a == '.':
      break

    for j in a :
    
     if j == '(' or j == '[' :
            stack.append(j)
    
     elif j == ')':
        if not stack or stack[-1] == '[':
            out.append("no")
            break
        else:
           stack.pop()
            
     elif j == ']':
        if not stack or stack[-1] == '(':
            out.append("no")
            break
        else:
            stack.pop()
            
     elif j == ".":
        if not stack:
            out.append("yes")
        else:
            out.append("no")
            
    stack=[]       

for i in out:
    print(i)
     
 

        
