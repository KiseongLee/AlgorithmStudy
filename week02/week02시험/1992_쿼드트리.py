n = int(input())

data=[]
for i in range(n):
    data.append(input())

ans = []

def recursive(size, x, y):
    
    num = data[x][y]
    
   
        
    for i in range(x, x+size):
        for j in range(y, y+size):
            
            if num != data[i][j]:
                
                ans.append("(")
                recursive(size//2, x, y)
                recursive(size//2, x, y+size//2)
                recursive(size//2, x+size//2, y)
                recursive(size//2, x+size//2, y+size//2)
                ans.append(")")
                return
                
                
            
    if num == "1":
        ans.append(1)
        
    else:
        ans.append(0)
    
    
    

recursive(n, 0, 0)
for i in range(len(ans)):
    ans[i] = str(ans[i])
    
print("".join(ans))