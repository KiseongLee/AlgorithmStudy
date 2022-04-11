'''

문제 : 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지 알아내는 프로그램 작성

입력 : 탑의 수 N [ 1, 500,000 ] // 탑들의 높이 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어짐. [1, 1억]

출력 : 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호(index)를 빈칸 사이에 두고 출력
      없으면 0을 출력
      
      
1. stack의 구조를 생각해서 한 번 풀어봅시다.

stack은 선입후출의 개념이다.
그렇게되면 흠
나는 4부터 체크를 해줘야한다.
4부터 체크를 해줘야 한다는 의미는 일단 스택에 다 있어야 한다는 거 아님?

6은 확인할 필요도 없고
9는 앞에것만 확인하면되고
5는 앞에앞에것만 확인하면되고
7
4 


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
        