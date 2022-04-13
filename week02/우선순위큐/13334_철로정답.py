# import sys
# import heapq

# n = int(input())
# road_info = []
# for _ in range(n):
#     road = list(map(int, input().split()))
#     road_info.append(road)

# d = int(input())
# roads = []
# for road in road_info:
#     house, office = road
#     if abs(house - office) <= d:
#         road = sorted(road)
#         roads.append(road)
        
# roads.sort(key=lambda x:x[1])

# 정보 받기
#--------------------------------------------------

# answer = 0
# heap = []
# for road in roads:
#     if not heap:
#         heapq.heappush(heap, road)
#     else:
#         while heap[0][0] < road[1] - d:
#             heapq.heappop(heap)
#             if not heap:
#                 break
#         heapq.heappush(heap, road)
#     answer = max(answer, len(heap))

# print(answer)
# 철로 놓기 및 개수 세기



'''
1) 먼저 각 사무실, 집 정보를 roads에 저장할 때 사무실과 집의 거리가 d보다 크다면 d를 어떻게 움직여도
포함될 수 없으므로 저장하지 않는다. d보다 작거나 같다면 좌표정보를 오름 차순으로 정렬해 저장해준다.

2) 철로의 시작점을 가장 작은 것부터 시작할 수 있도록 roads를 본인의 원소 중 큰 원소를 기준으로 
오름차순으로 정렬해준다. (앞서 말한 것처럼 더 멀리있는 좌표값에서 왼쪽으로 철로를 깔 것이기 때문에 더 멀리 있는 
좌표값(= 큰원소)가 시작점이 된다.)

3) 철로의 시작점을 가장 작은 것부터 순회하면서 차례대로 힙에 넣어주게 된다. 이 때 힙에 존재하는 가장 작은 값이
철로의 끝점안에 있는지 확인해 철로 내에 있지 않다면 힙에서 제거한다.





'''


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
                                            # 철로를 깔 때, 앞에 것부터 깔면서 가야하기 때문에

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