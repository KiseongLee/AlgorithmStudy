
t = int(input())



for _ in range(t):
    stack=[]
    data = list(input().strip())

    for i in data:
        
        if i == "(":
            stack.append(i)
        
        if i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
      
    else:
        
        if stack:
            print("NO")
        
        else:
             print("YES")
             


# 일단 for - else 구문 잘 몰라서 해맸고
# stack 만드는 위치 계속 초기화 해줘야하는 거 몰랐다.
# 두 개 체크하기
