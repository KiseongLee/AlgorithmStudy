import sys 
sys.setrecursionlimit(10**6) 

def append_star(LEN): 
    if LEN == 1: 
        return ['*'] 
    Stars = append_star(LEN//3) 
    L = [] 
    
    for S in Stars: 
        L.append(S*3) 
    for S in Stars: 
        L.append(S+' '*(LEN//3)+S) 
    for S in Stars: 
        L.append(S*3) 
    return L 

n = int(sys.stdin.readline().strip()) 
print('\n'.join(append_star(n)))



# 출처: https://cotak.tistory.com/38 [TaxFree]

# LEN = 3 이면 LEN = 1 로 바로 들어가서 ["*"] 찍고 for문 한 번
# LEN = 9 이면 LEN = 3이 되고 다시 LEN = 1이 된다.
# ["*"](LEN 1)(Stars에 넣어줌) 찍고 for문 한번 돈다. (LEN 3)
# return으로 L이 Start에 들어가게되고 LEN 3은 끝이난다
# 다시 L이 Start에 들어가게되고 (LEN9) 반복된다.



import sys
input = sys.stdin.readline
n = int(input())

def stars(n):
    
    if n == 1:
        return ["*"]
    
    star = stars(n//3)
    
    output = []
    
    for i in star:
        output.append(i*3)
    
    for i in star:
        output.append(i+" "*(n//3)+i)
    
    for i in star:
        output.append(i*3)
        
    return output

print("\n".join(stars(n)))
    
















