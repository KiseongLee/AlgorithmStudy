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