'''
문제 : N [1, 10000] 섬 , 중량제한, 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램 작성

입력 : N, M [1, 100000] // A,B,[1,N] C[1, 10억] (모든 다리의 방향은 양방향) 

출력 : 답 출력

'''

import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])                  
    graph[b].append([a,c])

distance = [0]*(n+1)                        
X,Y = map(int, input().split())             


def bfs(b, start):                          
    
    q = []
    heapq.heappush(q, [b, start])           
                                                                                                                              
    while q:
        
        cur_cost, cur_index = heapq.heappop(q)      
    
        if cur_index == Y:                      
            break                               
        if distance[cur_index] > -cur_cost:     
            continue    
                          
        for next_index, next_cost in graph[cur_index]:  
            
            if cur_cost == 0:                          
                distance[next_index] = next_cost        
                heapq.heappush(q, [-distance[next_index], next_index]) 
                continue   
            elif -cur_cost > next_cost and distance[next_index] < next_cost:  
                  distance[next_index] = next_cost
                  heapq.heappush(q, [-distance[next_index], next_index])
                
            elif -cur_cost <= next_cost and distance[next_index] < -cur_cost:
                 distance[next_index] = -cur_cost
                 heapq.heappush(q, [-distance[next_index], next_index])
               
                    
bfs(0, X)               
print(distance[Y])