
n = int(input())

data = [list(map(int, input())) for _ in range(n)]
ans = []


def recursive(size, x, y):
    
    
    
    num = data[x][y]
    
    
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            
            if num != data[i][j]:           
             
             ans.append("(")
             recursive(size//2, x, y)
             recursive(size//2, x, y + size//2)
             recursive(size//2, x + size//2, y)
             recursive(size//2, x + size//2, y + size//2)
             ans.append(")")
             return
    
         
    if num == 0:
        ans.append(0)
    else:
        ans.append(1)
      
            
                                 
             
    

recursive(n, 0, 0)

ans =[str(a) for a in ans]
ans = ("".join(ans))


print(f"{ans}")