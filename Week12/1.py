tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
		

from collections import deque

def solution(tickets):    
    
    tickets.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(tickets)):
        if "ICN" == tickets[i][0]:
            if bfs(tickets[i][0],tickets[i][1], i, tickets):
                return bfs(tickets[i][0],tickets[i][1], i, tickets)
            


def bfs(start, end, i, tickets):
    
    visited = [0]*len(tickets)
    q = deque()
    q.append([start,end])
    ans = [start]
    visited[i] = 1
        
    while q:
        start, end = q.popleft()
        
        for i in range(len(tickets)):
            if end == tickets[i][0] and not visited[i]:
                visited[i] = 1
                ans.append(tickets[i][0])
                q.append(tickets[i])
                break
       
    if all(visited):
        ans.append(end)
        return ans
    else:
        return

        

print(solution(tickets))

