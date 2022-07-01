# 10분 - 어떻게 풀지?, dp를 어떻게 사용해야할지 감이 안왔다.
# 1분 - 그냥 for문 돌려서 1개씩 체크하는 것도 방법일듯
# 3분 - 어떻게 구할지 생각해봄
# 5분 - 손코딩함 -> 근데 굳이 왜함 ? 시간 오래걸리는데, 막판에 조건 어떻게 할지 헷갈림
# 3분 - 다시 생각을 해봄 어떻게하면 조건을 걸 수 있을지, 근데 여기서부터 약간 답답함 느낌
# 5분 - 뭐했지 라는 생각 들다시피 처음부터 생각을 해봤지만 답이 안나옴
# 5분 - for문 조건 나눔
# -> 1개 기준 - 기준 넘어가면 - 2번째 기준으로 돌림
# -> 1개 기준 - 기준 못넘어가면 - 1번째 기준으로 다시 돌림
# 구현이 안됨, for문 썼는데 기준이 바뀌는데 어떻게 하지?
# 그리고 이게 맞나 생각이 조금 듬..
# 마지막 5분만 구현해보고 그만하자라는 생각이 듬
# 5분 - 구현 못하고, 했어도 틀린 설계라 어차피 틀렸음 시간낭비...

n = int(input())

data = sorted([sorted(map(int, input().split())) for i in range(n)])

dp = [1]*(n)

# count = 0
# i=0
# while True:
#     for j in range(1, len(data)-1):
#         if (data[i][0] >= data[j][0] and data[i][1] >= data[j][1]) or
#             (data[i][0] >= data[j][1] and data[i][1] >= data[j][0])
        
#             count += 1
#             i = j
#             break
    
#     if j == len(data)-1:
#         break

# dp[n] == dp[0] ~ dp[n-1] 중에서 가능한 것 + 1 
# 갱신!!

for i in range(1, n):
    for j in range(i):
        if data[i][1] >= data[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)
print(max(dp))

# 내가 푼 풀이로 통과가 안됨...왜 그렇지에 대한 생각을 좀 해봐야할듯
# 나는 거꾸로 정렬을 했고 값을 비교해줬는데 왜???
# 정렬을 순서대로 해줘야 하는 듯 하다 정확히 어떻게 반례가 생성되는지는 모르겠는데 어쨌든 비교할 범위를 줄이면서 정렬을 해줘야하는게 맞다.


n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((max(a,b), min(a,b)))

dp = [1]*(n)

data.sort(reverse=True)

for i in range(1, n):
    for j in range(i):
        if ((data[i][0] <= data[j][0] and data[i][1] <= data[j][1]) or
             (data[i][1] <= data[j][0] and data[i][0] <= data[j][1])):
            dp[i] = max(dp[i], dp[j]+1)
            # print(dp)
# print(dp)
print(max(dp))