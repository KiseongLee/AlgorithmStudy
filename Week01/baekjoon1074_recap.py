# n, r, c = map(int, input().split())

# ans = 0

# while n != 0:
    
#     n -= 1

#     if r < (2**n) and c < (2**n):
    
#         ans += (2**n) * (2**n) * 0


#     elif r < (2**n) and c >= (2**n):
    
#         ans += (2**n) * (2**n) * 1
#         c -= (2**n)

#     elif r >= 2**n and c < 2**n:
    
#         ans += (2**n)*(2**n)*2
#         r -= (2**n)

#     else:
    
#         ans += (2**n) * (2**n) * 3
#         r -= (2**n)
#         c -= (2**n)

# print(ans)
 


n, r, c = map(int, input().split())


def find_num(n, r, c):
    
    if n == 1:
        return find_q(n, r, c)
    
    result = find_q(n, r, c)
    if result == 0:
        
        return find_num(n-1, r, c)
        
    elif result == 1:
        
        return (2**(n-1))*(2**(n-1)) + find_num(n-1, r, c - 2**(n-1))
        
    elif result == 2:
        
        return (2**(n-1))*(2**(n-1))*2 + find_num(n-1, r- 2**(n-1), c)
        
    else:
        
        return (2**(n-1))*(2**(n-1))*3 + find_num(n-1, r- 2**(n-1), c - 2**(n-1))
        


def find_q(n,r,c):
    
    num = 2**(n-1)
    
    if (r < num) and (c < num):
        return 0
    
    elif (r < num) and (c >= num):
        return 1
    
    elif (r >= num) and (c < num):
        return 2
    
    else: 
        return 3

print(find_num(n,r,c))