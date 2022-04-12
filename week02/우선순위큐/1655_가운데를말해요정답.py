'''

1. leftheap과 rightheap의 길이가 같다면 ( 즉 두 heap에 들어있는 리스트 요소 수가 같으면) 중간값의 기준이 되는 leftheap에 수를 넣는다.
   반면, 길이가 같지 않다면 길이를 맞춰주기 위해 rightheap에 수를 넣는다.
   
2. 만약에 leftheap의 루트가 rightheap의 루트보다 크면 leftheap의 루트와 rightheap의 루트를 바꿔준다.

why ? leftheap은 중간값을 기준으로 작은 수가 들어가는 곳이다. 그런데 leftheap의 루트가 rightheap보다 크다면,
중간값보다 큰수가 leftheap에 들어가 있는 상황이기에 leftheap의 루트와 rightheap의 루트를 바꿔준다.

'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())

leftheap = []
rightheap = []
answer = []

for i in range(n):
    
    inputNum = int(input())
                                                                # 왼쪽 힙이 항상 더 많아야 함 (= 짝수 일 때, 작은 값이 나와야 하기 때문에)
    if len(leftheap) == len(rightheap):                         # 왼쪽 힙과 오른쪽 힙이 같으면
        heapq.heappush(leftheap, (-inputNum, inputNum))         # 왼쪽힙에 값을 넣는다
    else:                                                       # 아니면
        heapq.heappush(rightheap, (inputNum, inputNum))         # 오른쪽힙에 값을 넣는다.
    
    if rightheap and leftheap[0][1] > rightheap[0][0]:          # 오른쪽 힙이 있고, 왼쪽 힙의 가장 큰 값과 오른쪽 힙의 가장 작은 값을 비교한다면    
        min = heapq.heappop(rightheap)[0]                       # 작은 값은 오른쪽 힙에 있는 값이고
        max = heapq.heappop(leftheap)[1]                        # 큰 값은 왼쪽 힙에 있는 값이고    
        heapq.heappush(leftheap, (-min, min))                   # 서로 바꿔 줘서 넣어준다.
        heapq.heappush(rightheap, (max, max))
    
    print(leftheap[0][1])                              # 왼쪽 힙 가장 아래의 값을 출력하면 된다.
    

# https://art-coding3.tistory.com/44





