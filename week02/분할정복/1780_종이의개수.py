n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

a = 0
b = 0
c = 0
def recursive(size, x, y):
    
    global a, b, c


    num = data[x][y]
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            
            if num != data[i][j]:           #key point 시작 하는 값과 같은지만 보면 된다.
    
             recursive(size//3, x, y)
             recursive(size//3, x, y+ size//3)
             recursive(size//3, x, y + size//3*2)
             recursive(size//3, x + size//3, y)
             recursive(size//3, x + size//3, y+ size//3)
             recursive(size//3, x + size//3, y + size//3*2)
             recursive(size//3, x + size//3*2, y)
             recursive(size//3, x + size//3*2, y+ size//3)
             recursive(size//3, x + size//3*2, y + size//3*2)
             
             return                        
             
    if num == -1:
        a += 1
    elif num == 0:
        b += 1
    else:
        c += 1
                 

recursive(n, 0, 0)

print(a)
print(b)
print(c)