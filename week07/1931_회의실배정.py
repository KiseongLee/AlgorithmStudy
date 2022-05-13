n = int(input())

time = []
for _ in range(n):
    time.append(tuple(map(int, input().split())))

time.sort(key=lambda x : (x[1], x[0]))

count = 1
X = time[0][1]

for j in range(1, n):
    if X <= time[j][0]:
       X = time[j][1]
       count += 1
      

print(count)


# 1. 정렬 x[0] 해줘야함
# 2. X로 놓는 skill --> 비교할 때, for문 굳이 2개 돌릴 필요가 없다
# 3. 같을 수도 있다. 같아도 배치가 가능하니 처리해줘야한다.