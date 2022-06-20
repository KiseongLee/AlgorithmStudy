# A->B (40분)

# 처음에는 DP로 접근해야 하다가, 거꾸로 생각하면 되구나해서 조건 걸었었는데
# 두 경우를 비교해줘야해서 조금 헷갈렸는데, 조건을 각각 걸어줘서 풀 수 있었습니다.
# 조금 더 좋은 풀이가 있으면 참고하겠습니다.


# A, B = map(int, input().split())

# tmp = 0
# count = 1
# curr = 1e9
# while True:
    
    
#     if B == A:
#         print(count)
#         break
    
#     if B < A:
#         print(-1)
#         break
        
#     if B % 2 == 0:
#         if (B-1) % 10 == 0:
#           B = min(B//2 , (B-1)//10)
#           count += 1  
#         else:
#             B = B//2
#             count += 1
#     else:
        
#         if (B-1) % 10 == 0:
#             B = (B-1)//10
#             count += 1 
#         else:
#             print(-1)
#             break  
    
    
# bfs 풀이
# deque 활용, 순서가 상관없음 어차피 count를 가지고 들고가므로 따져줄 필요 없고
# 같을 떄, 그냥 어차피 제일 먼저것이(최소것) 나오므로 그냥 뽑아내면된다

# 여기서 출력할 때, res = -1로 하는 것 괜찮은 방법인 것 같다 !!

from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])

res = -1

while q:
    
    
    a, cnt = q.popleft()
    
    if a == b:
        res = cnt
        break
    
    if a*2 <= b:
        q.append([2*a, cnt+1])
    if int(str(a)+"1") <= b:
        q.append([int(str(a)+"1"), cnt+1])

print(res)