import heapq
def solution(sco, K):
    heap = []
    count = 0
    for i in range(len(sco)):
        heapq.heappush(heap, sco[i])
    
    x = heapq.heappop(heap)
    if x >= K:
        return 0
    while heap and x < K:
        y = heapq.heappop(heap)
        z = x + (y*2)
        count += 1
        heapq.heappush(heap, z)
        x = heapq.heappop(heap)
    if x >= K:
        return count
    else:
        return -1

sco = [1, 2]
K = 7
print(solution(sco,K))

# 내풀이(22.08.30)
import heapq
def solution(sco, K):
    heap = []
    count = 0
    for i in sco:
        heapq.heappush(heap, i)
        
    x = heapq.heappop(heap)    
    while x < K:
        if not heap:
            return -1
        y = heapq.heappop(heap)
        z = x + (y*2)
        heapq.heappush(heap, z)
        count += 1
        x = heapq.heappop(heap)
    return count