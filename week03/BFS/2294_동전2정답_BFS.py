from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
check = [0 for _ in range(k+1)]
q = deque()

for coin in coins:      
    if coin > k :       # 코인이 애초에 k보다 크면 바로 다음으로 넘어감
        continue    
    q.append([coin, 1])
    check[coin] = 1

flag = True                     # 불가능한 경우를 위해 flag 정의
while q:                        # q가 있을 때까지 반복문 실행
    value, count = q.popleft()  # value, count 값을 queue에서 빼준다
    
    if value == k:              # 만약 value와 k가 일치하다면
        print(count)            # 바로 카운트 출력
        flag = False            # flag는 False로 변경
        break
    
    for coin in coins:          # 코인값 for문 실행
        if value + coin > k:    # value + coin 값이 k보다 크다면
            continue            # 바로 다음 순서로 넘어가자
        if check[value+coin] == 0:  # 그 외, check 값이 0이라면(전에 나온 것이 아니라면)
            check[value+coin] = 1   # 방문 체크 해주고
            q.append([value+coin, count+1]) # 그 값들과 count값을 올려준 것을 q에 넣어준다.


if flag:
    print(-1)
    
    
    #https://alpyrithm.tistory.com/81