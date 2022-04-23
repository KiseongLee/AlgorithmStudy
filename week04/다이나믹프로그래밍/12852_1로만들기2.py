# 답 본 문제는 처음 부터 다시 구현해보기 - 재관이형 말씀 참고!!

n = int(input())

dp =[0] * (n+1)
result = [0] * (n+1)

for i in range(2, n+1):
    
    dp[i] = dp[i-1] + 1
    result[i] = i-1
    
    if i % 2 == 0 and dp[i//2]+1 < dp[i]:
         dp[i] = dp[i//2]+1
         result[i] = i //2
         
    if i % 3 == 0 and dp[i//3]+1 < dp[i]:
        dp[i] = dp[i//3]+1
        result[i] = i // 3
  
print(dp[n])

print(result)

while n != 0:
    print(n, end=' ')
    n = result[n]


# print(result[n] + result[result[n][-1]] + result[result[result[n][-1]][-1]] + result[result[result[result[n][-1]][-1]]])


# 새로운 배열을 받아서 값을 하나씩 넣어주면되는데
# 이게 왜 되냐면
# for 문 돌 때, 어차피 무조건 가장 최소가 되는 값을 향해 가는데 딱 1번 해줄 수 있음
# 그래서 이걸 타고 타고 가면 출력할 수 있다는 생각을 해야한다.
# 제일 많이 값을 적게하는 쪽을 뒤쪽에 두면 되겠지?

# 이게 진짜 어려웠던 것이
# dp[i//2] + 1 < dp[i] 조건을 걸어야 무조건 나누기를 하지 않는다.
# 그래서 이게 완벽한 풀이가 되는 것이다.


