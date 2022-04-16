# 21606 아침 산책
from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
inner_outer = input().rstrip()
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def n_comb_2(n):
    return n*(n-1)//2

total_cnt = [0]
visited = [0]*(N+1)
root_queue = deque()

def how_many_path(root):
    now_cnt = []
    # BFS
    queue = deque([(root, None)])
    while queue:
        now_node, group_num = queue.popleft()
        for adj_node in adj_list[now_node]:
            if not visited[adj_node]:
                visited[adj_node] = 1
                if inner_outer[adj_node-1] == '0': # 실외
                    if group_num is None:
                        now_cnt.append(0)
                        queue.append((adj_node, len(now_cnt)-1))
                    else:
                        queue.append((adj_node, group_num))
                else: # 실내
                    if group_num is not None:
                        now_cnt[group_num] += 1
                    else:
                        total_cnt[0] += 1
                    root_queue.append(adj_node)
    
    for cnt in now_cnt:
        total_cnt[0] += cnt + n_comb_2(cnt)


for node in range(1, N+1):
    if inner_outer[node-1] == '1':
        root_queue.append(node)
        visited[node] = 1
        break

while root_queue: # 메모리 줄이려고
    root = root_queue.popleft()
    how_many_path(root)

print(total_cnt[0]*2)