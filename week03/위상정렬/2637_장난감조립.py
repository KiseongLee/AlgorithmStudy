from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

graph = [[] for i in range(v+1)]
indegree = [0] * (v+1)
count = [[0]*(v+1) for i in range(v+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    graph[b].append((a,c))                          # graph에 개수까지 넣어준다는 것이 굉장히 key point이다.
                                                    # 처음에 나는 아예 따로 받았었다. list 생성해서 index에 번호랑 개수 때려박음
                                                    # 이를 적용을 어떻게 할지 처음에 몰랐다.
                                                    # 6으로 갔을 때, 5를 전에 있는 값으로 교체만 해줬으면 됬는데 그게 어려웠음
                                                    
    indegree[a] += 1
    

def topology():
    
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for i, j in graph[now]:                         # 핵심 key:
            if count[now].count(0) == v+1:              # 기본 템이면 당연히 0의 개수가 v+1이겠지
                count[i][now] += j                      # 그러면 해당 인덱스의 now값에 그냥 더해주면된다.
            else:
                for k in range(1, v+1):                 # 기본 템이 아니라면 하나씩 검사하면서
                    count[i][k] += count[now][k] * j    # 해당하는 인덱스 부분에 값의 개수만큼을 곱해주면된다.
                                                        # 5가 1, 2 2개씩으로 이루어져 있으니까
                                                        # 6에 5가 2개 들어간다 하면
                                                        # count[6][1] += count[5][1]*2
                                                        # count[6][2] += count[5][2]*2
                                                        # count[6][3] += count[5][3]*2 --> count[5][3]=0이므로 의미없음
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for x in enumerate(count[v]):               # enumerate([A,B,C])
                                                # (0,A), (1,B), (2,C)
        if x[1] > 0:                            # x[1]은 튜플의 뒷부분이므로 개수가 되겠지
            print(*x)                           # 0보다 크면 
                                                # x를 unpack(*)해서 프린트 해줘라.
topology()




# 최종적으로 필요한 부품에서 그 전에 있는 값들을 싹 받아와야 한다는 생각을 해내야함
# 그리고 하나씩 업데이트 해가면서 추가해주면 되는데
# 기본 부품은 그러면 다 0으로 이루어져 있을 것이고
# 중간 부품은 숫자가 좀 채워져 있겠지.
# 그러면 둘로 나눠서 큐에서 뽑아 낼 때, 조건을 걸어주면 되겠다는 생각을 해야함.
# 기본템이면 0의 개수가 v+1 --> 해당 인덱스의 기본템자리에 개수만 더해주면 되고
# 중간템이면 그 외라고 해놓고 --> 해당 인덱스의 처음부터 끝까지 가중치(개수)를 곱해서 더해주면 된다.

# 출력할 때, 스킬이 있는데
# enumerate, * 등 위에 써있다. 참고