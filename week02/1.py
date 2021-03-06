import heapq
import sys
input = sys.stdin.readline

n = int(input())                            # 사람의 수 입력

data=[]                                     # 집, 사무실 위치 정보 리스트로 받기
for _ in range(n):
    x = list(map(int, input().split()))
    data.append(x)
    
l = int(input())                            # 철로 길이 받기

data2 = []                                  # 정렬 해줄 데이터를 모아 둘 리스트 만들기 
                                            #(새로 만드는 이유는 철로 길이보다 긴 거리에 있는 것을 제외하기 위해)

for i in data:
    h, o = i                                # 집, 사무실 위치 각각 받기
    
    if abs(h-o) <= l:                       # 절댓값을 구해서 l보다 작으면 넣어주자
        i = sorted(i)                       # (h,o) 순서쌍을 오름 차순 해주자 --> 철로 길이 안에 집, 사무실 다 들어와야하기때문에
                                            # 오름 차순으로 해야 나중에 식을 넣었을 때, 문제가 안생김
        data2.append(i)                     # 걸러진 데이터를 새로운 리스트에 넣어주자
        
data2.sort(key=lambda x : x[1])             # key point : 받은 데이터를 끝에 거리를 기준으로 오름차순으로 해줌 
                                            # 철로를 깔 때, 앞에서부터 깔면 예외가 발생한다
                                            # 예외 케이스 ) 1 4 / 1 4 / 2 5 / 3 4 answer:3 / 앞에것 오름차순하면 answer:2
print(data2)
answer = 0
heap = []

for i in data2:                             # 1명의 집, 사무실 하나씩 확인
    if not heap:                            # 힙이 없다면
        heapq.heappush(heap, i)             # 바로 힙에 넣어준다
    
    else:
        
        while heap[0][0] < i[1] - l:        # 힙에 있는 시작점이 가장 작은 값의 위치 < 들어오는 것에서 철로의 길이를 뺀 값이면 
            heapq.heappop(heap)             # 힙에 있는 가장 작은 값의 위치가 철로에 포함이 되지 못한다는 것이고, pop해준다
            if not heap:                    # 뺐는데 힙에 아무것도 없으면 바로 break 해준다. 비교할 게 없기 때문
                break
        heapq.heappush(heap, i)             # while문에 안들어가면 즉, 위에 조건이 만족하지 않으면 철로에 포함이 될 수 있으므로 push
    answer = max(answer, len(heap))         # heap에 들어가 있는 것은 heap의 길이기 때문에 비교를 계속해주면서 답을 구해낸다.

print(answer)