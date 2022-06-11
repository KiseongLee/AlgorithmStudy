# 2563_색종이(백준)

# 문제 자체는 쉬워보였으나, 계속해서 머릿속으로 수학 계산만 하고있었다.
# 사실 그래프 형태로 생각하여 1로 다 바꿔주면 되었는데 생각을 조금 편협하게 함
# 구현 문제 -> 넓이 -> 1로 바꿔서 생각 -> 다 count해주면 되겠는데?
# 범위 헷갈림 -> 총 10개인데 당연히 10을 더해줘야는데, 첫문자값 때문에 조금 헷갈렸다.


n = int(input())

graph = [[0]*101 for _ in range(101)]

for _ in range(n):
    b, a = map(int, input().split())

    for i in range(10):
        for j in range(10):
            graph[a+i][b+j] = 1



count = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
       if graph[i][j] == 1:
           count += 1

print(count) 


