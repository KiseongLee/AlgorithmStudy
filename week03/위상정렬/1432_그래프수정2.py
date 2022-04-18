import heapq

n = int(input())

graph = [[] for _ in range(n+1)]

outdegree = [0]*(n+1)

result = [0]*(n+1)

for i in range(1, n+1):
    connection = list(map(int, input()))
    
    for idx, val in enumerate(connection):
        if val == 1:
            graph[idx + 1].append(i)
            outdegree[i] += 1               # 나가는 것에 1을 더해주는 outdegree를 만든다.
            

def topology_sort(n):
    
    heap = []
    
    for i in range(1, n+1):
        if outdegree[i] == 0:
            heapq.heappush(heap, -i)
            
    while heap:
        
        now = -heapq.heappop(heap)
        result[now] = n
        
        for connected_node in graph[now]:
            outdegree[connected_node] -= 1
            if outdegree[connected_node] == 0:
                heapq.heappush(heap, -connected_node)
        
        n -= 1

topology_sort(n)

if result.count(0) > 2:
    print(-1)

else:
    print(' '.join(map(str, result[1:])))
    
# 왜 최소힙으로 차례차례 넣어주면 안될까?
# 테스트 케이스
'''
4
0011
0000
0000
0100

기존 알고리즘의 결과 : 1 4 2 3
참고해 고친 알고리즘의 결과(정답) : 1 3 4 2

간선 3개짜리 간단한 그래프이나, 두 알고리즘의 차이점을 알 수 있었다.
기존 알고리즘은 1정점을 먼저 취하고, 그로 인해 indegree=0인 정점 두개(3,4)가 남았을 때 greedy하게 3을 택하는 바람에 2정점의 순서가 뒤로 밀려 버렸다. 
그에 반해 고친 알고리즘은 outdegree=0인 정점(2,3)부터 취하는데, 
이 때 큰 값부터 우선순위 큐가 뱉어주므로 3정점을 취한다. 그리고 3정점은 가장 큰 번호를 배정해준다.(N=4) 
그 다음 outdegree=0인 정점은 2정점 밖에 없으므로 그 다음 값인 3을 배정해준다. 
비록 두번째로 큰 번호를 배정받긴 했지만 최적값임에 놀랐다. 그 다음 차례대로 4정점 1정점 순으로 점점 작은 번호를 배정해준다.
'''

# 왜 사이클이 발생하면 result 값은 바뀌지 않을까? --> 정점들이 큐에 들어갈 수가 없다. outdegree의 값이 0이 되야 들어가는데 들어가지 못함


# 참고 사이트

# https://velog.io/@stthunderl/%EB%B0%B1%EC%A4%80-1432-%EA%B7%B8%EB%9E%98%ED%94%84%EC%88%98%EC%A0%95-python-%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC
# https://velog.io/@whddn0221/%EB%B0%B1%EC%A4%80-1432-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%88%98%EC%A0%95-%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-mrltwcp5#%EB%8D%94-%EC%95%8C%EC%95%84%EB%B3%BC-%EA%B2%83
# https://syogeng.wordpress.com/2017/09/06/test/

