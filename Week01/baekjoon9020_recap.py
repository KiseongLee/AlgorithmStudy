import math
t = int(input())

def prime(x):

    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        
    return x

for i in range(t):
    
    x = int(input())
    
    prime_set=[]
    
    for i in range(x):
        
        if prime(i) != False:
            
            prime_set.append(prime(i))
        
    a = x // 2
    b = x // 2
    
    while (not a in prime_set) or (not b in prime_set):
        
        a += 1
        b -= 1
    
    print(b, a)
        



