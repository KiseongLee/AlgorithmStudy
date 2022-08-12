# 124 나라의 숫자


def solution(n):
    ans =[]
    ans2 = []
    while True:
        x = n // 3 
        y = n % 3
        
        if y == 0:
            x = x-1
            y = 3
            
        ans.append(y)
        n = x
        if x == 0:
            break
    
    for i in range(len(ans)-1,-1,-1):
       if ans[i] == 3:
          ans[i] = 4
       if ans[i] == 2:
          ans[i] = 2
       if ans[i] == 1:
          ans[i] = 1
            
       ans2.append(str(ans[i]))
    
    x = ''.join(ans2)
    print(x)
    return x