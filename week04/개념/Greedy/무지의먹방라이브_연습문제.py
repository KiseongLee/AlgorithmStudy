
import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
     heapq.heappush(q, (food_times[i], i))
       
    while True:
        
        food_time, food_index = heapq.heappop(q)
        
        if k <= food_time * len(food_times):
            heapq.heappush(q, (food_time, food_index))
            break
       
        for i in range(len(food_times)):
            food_times[i] -= food_time
        k -= food_time * len(food_times)
           
    q.sort(key=lambda x: x[1])   
    idx = k % len(q)
    return q[idx][1]+1

food_times = list(map(int, input().split()))
k = int(input().rstrip())
print(solution(food_times, k))

# 우선순위 큐에 food_times, food_index 넣어주기
# q라고 정의를 하고 넣으면 되겠지. for문을 통해서

# 우선순위 큐 앞에 들어 오는 것의 계산을 위해서 --> heappop으로 하면될듯 *  len(food_times) 각각 food_times에서 빼준다

# 그리고 food_times 갱신 해주고, k 값을 빼야지
# if 그리고 heappop * len(food_times)와 k를 비교해서 k가 작으면 바로 
# k를 음식 개수인 len(q)나눈 나머지로 체크해서, 나머지-1 이 index가 되겠다. 


