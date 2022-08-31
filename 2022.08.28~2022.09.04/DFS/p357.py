tickets = [["JFK","SFO"],["JFK", "ATL"], ["SFO", "ATL"], ["ATL","JFK"],["ATL", "SFO"]]

tickets.sort()
result=["JFK"]
for i in range(len(tickets)):
    if tickets[i][0] =="JFK":
        for j in range(len(tickets)):
            if tickets[i][1] == tickets[j][0]:
                A = tickets.pop(i)
                break

def dfs(end):
    
    result.append(end)
    
    for i in range(len(tickets)):
        if tickets:
            if tickets[i][0] == end:
                X = tickets.pop(i)
                dfs(X[1])
                
dfs(A[1])
print(result)


# dfs 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
                while graph[a]:
                    dfs(graph[a].pop(0))
                route.append(a)
        dfs('JFK')
        return route[::-1]