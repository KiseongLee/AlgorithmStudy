'''

문제 : 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지 알아내는 프로그램 작성

입력 : 탑의 수 N [ 1, 500,000 ] // 탑들의 높이 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어짐. [1, 1억]

출력 : 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호(index)를 빈칸 사이에 두고 출력
      없으면 0을 출력
      
      
1. 일단 for문으로 앞서는 모든 부분을 검색하고, 큰 것이 나오는 순간 break를 걸어서 for문이 빠져나오도록 구현할 것


'''


'''시간초과 풀이'''
import sys
input = sys.stdin.readline

n = int(input())



stack = list(map(int, input().split()))

ans = []

max_value = stack[-1]

for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        max_value = stack[i]
        if stack[j] > max_value:
            ans.append(j+1)
            break
    else:
        ans.append(0)


for i in range(len(ans)-1, -1, -1):
    print(ans[i], end=" ")


        
    

        