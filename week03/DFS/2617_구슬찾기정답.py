'''
문제의 핵심은 dfs로 다 경로를 뽑아낼 생각을 하지 말고, 문제에서 준 힌트를 바탕으로 생각해야한다.
--> 어떻게하면 다 뽑아낼 지 생각만 하다가 끝났음. / 그리고 start라는 집합을 만들어서 작은 것부터 시작해야하는 것을 뽑아내려고 했었음.

문제에서 예시로 준 구슬들에서

1번 구슬, 4번 구슬은 무게가 중간인 구슬이 절대 될 수 없다는 것을 확실히 알 수 있다.
1번 구슬보다 무거운 것이 2,4,5번 구슬
4번 보다 가벼운 것이 1,2,3번이다. --> 따라서 답은 2개이다.

이 것을 그대로 코드로 옮겨서 치면된다.

여기서 무거운 것, 가벼운 것 두개가 나오므로 이를 2번 탐색해줘야한다는 것이 핵심 key이다.



'''



def dfs(graph, v):
    global count
    visited[v] = True
    # count += 1                    # 처음에 들어오는 값 count 세면 안됨
    
    for i in graph[v]:
        if not visited[i]:
            count += 1              # 카운트 값 위치 중요!!! 위쪽 visited[v]에 넣으니까 틀림
                                    # 처음에 들어오는 값이 count가 세어지면 안된다.
            dfs(graph, i)
    
    return count



n, m = map(int, input().split())

light = [[] for _ in range(n+1)]        # 무게가 작은 순 부터 
heavy = [[] for _ in range(n+1)]        # 무게가 큰 순 부터

for i in range(m):
    a, b = map(int, input().split())
    light[b].append(a) # 무게가 작은 순
    heavy[a].append(b) # 무게가 큰 순

result = 0
for i in range(1, n+1):                 # 핵심 key 
    visited = [False]*(n+1)             # 방문처리는 for문 돌 때마다 초기화
    count = 0                           # count도 for문 돌 때마다 초기화
    if dfs(light, i) >= (n+1) // 2:     # dfs(light) 작은 순부터 다 돌렸을 때, count값이 중간 값보다 같거나 많으면
        result += 1                     # 결과 값에 +1
    count = 0                           # count값 초기화
    if dfs(heavy, i) >= (n+1) //2 :     # dfs(heavy) 큰 순부터 다 돌렸을 떄, count값이 중간 값보다 같거나 많으면
        result += 1                     # 결과 값에 +1
        
print(result)                           
    





# 출처 : https://nyeongnyeong.tistory.com/208


