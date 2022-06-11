# D기준, S기준, L기준, R기준 다 따로 가면서
# 체크해줄 것은 체크해주면서 가는게 생각보다 괜찮네
# 그리고 딱 뽑을 것들만 가고 -> 하나를 뽑으면 다시 DSLR 기준으로 돌면서 문제를 푸는 과정
# 여기서 중요한건 L, R을 어떻게 하면 간단하게 해줄 수 있느냐 -> 수식으로 가야함
# L : num%1000 * 10 

from collections import deque


def bfs(start, end):
    q = deque([[start, ""]])
    visited = [0] * 10000
    visited[start] = True

    while q:
        num, operation = q.popleft()

        if num == end:
            return operation

        # D
        if not visited[num * 2 % 10000]:
            visited[num * 2 % 10000] = True
            q.append([num * 2 % 10000, operation + "D"])
        # S
        if not visited[(num - 1) % 10000]:
            visited[(num - 1) % 10000] = True
            q.append([(num - 1) % 10000, operation + "S"])
        # L
        if not visited[num % 1000 * 10 + num // 1000]:
            visited[num % 1000 * 10 + num // 1000] = True
            q.append([num % 1000 * 10 + num // 1000, operation + "L"])
        # R
        if not visited[num % 10 * 1000 + num // 10]:
            visited[num % 10 * 1000 + num // 10] = True
            q.append([num % 10 * 1000 + num // 10, operation + "R"])





T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))