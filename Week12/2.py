# from collections import deque

# def solution(tickets):    
#     tickets.sort()
#     for i in range(len(tickets)):
#         if "ICN" == tickets[i][0]:
#             if bfs(tickets[i][0],tickets[i][1], i, tickets):
#                 return bfs(tickets[i][0],tickets[i][1], i, tickets)
            


# def bfs(start, end, i, tickets):
    
#     visited = [0]*len(tickets)
#     q = deque()
#     q.append([start,end])
#     ans = [start]
#     visited[i] = 1
        
#     while q:
#         start, end = q.popleft()
        
#         for i in range(len(tickets)):
#             if end == tickets[i][0] and not visited[i]:
#                 visited[i] = 1
#                 ans.append(tickets[i][0])
#                 q.append(tickets[i])
#                 break
       
#     if all(visited):
#         ans.append(end)
#         return ans
#     else:
#         return

tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]

def solution(tickets):
    tickets.sort(reverse=True) # 정렬
    routes = dict() # {} 생성
    #그래프 생성
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    print(routes)

    
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        # 해당 나라가 graph에 없거나, 해당 나라의 키의 값이 0이면 (더 갈데가 없다는 뜻)
        if top not in routes or len(routes[top])==0:
            
            ans.append(st.pop()) # 해당 나라를 빼서 답안에 넣는다

        else: # 아니면 더 갈 곳을 찾는다 (해당 나라의 키의 값을 stack에 넣음)
            st.append(routes[top].pop())

    ans.reverse()
    return print(ans)

solution(tickets)