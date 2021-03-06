'''

문제 : 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지 알아내는 프로그램 작성

입력 : 탑의 수 N [ 1, 500,000 ] // 탑들의 높이 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어짐. [1, 1억]

출력 : 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호(index)를 빈칸 사이에 두고 출력
      없으면 0을 출력
      
      
1. stack의 구조를 생각해서 한 번 풀어봅시다.

입력 :
5
6 9 5 7 4

stack의 구조를 생각해보면

1.
stack : 6
ans : 0

2. 
9 > 6
이므로 6을 빼버리자 이후에도 9만 보일 것이기 때문에 (while을 써줘야한다는 것을 명심, 나보다 작은것이 있으면 다 빼버리자)
ans는 순서이므로 없는것은 0이다.
stack : 9
ans : 0 0

3. 
9 > 5이므로
일단 넣어준다. 왜냐하면 내 뒤에 나보다 작은 것이 들어올 수 있기 때문이다.
stack : 9 5
ans : 0 0 2

4. 
7 > 5 이므로
5를 빼준다. 
9> 7 이므로
7을 넣어준다.

stack : 9 7
ans : 0 0 2 2

5. 
7 > 4 이므로
4를 넣어준다.(뒤에 나보다 작은놈이 올 수 있기 때문에)

stack : 9 7 4
ans : 0 0 2 2 4

'''


import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
stack =[]
ans = []

for i in range(n):

    if stack:   
      while stack[-1][1] < a[i]:
          stack.pop()
          if not stack:
            stack.append([i, a[i]])
            ans.append(0)
            break    
      
      else:
          
          ans.append(stack[-1][0]+1)        #이 부분을 빼낼 때, 인덱스랑 같이 넣는 생각을 하지 못하였다. 참고부탁
          stack.append([i, a[i]])
          
          
    else:
        stack.append([i, a[i]])
        ans.append(0)


for i in range(len(ans)):
    print(ans[i], end=" ")
        