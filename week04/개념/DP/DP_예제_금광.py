'''
1. dp 테이블을 2차원으로 갱신할 생각을 못함. x값을 받아오려하다가 복잡해져버림

2. 기준을 앞에걸로 생각함. 다이나믹프로그래밍은 점화식을 쓸 때, 현재 값을 기준으로 앞에 걸 빼기로 계산함

3. 왼쪽 위 왼쪽 아래를 처리할 때, 나는 넘어가면 없애기로 할려고 했는데 답에서는 아니었음
   2개만 분리해줘서 경우만 나눠주면 됨
   
4. 한줄로 입력받는 것 분리하는 방식 배워놓기
    dp = []
    index =0
    for i in range(n);
      dp.append(array[index:index+m])
      index += m
    꼭 i를 안써도 되는구나 알아놓기!
'''

t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    data = list(map(int, input().split()))

    dp=[[]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i].append(data[4*i+j])       # 바로 dp테이블을 만들어 버린다


    for j in range(1, m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)


    '''
    first = []
    for i in range(n):
        first.append(data2[i][0])     # 첫번째 값을 받을 필요가 없고

    max_value = 0                   # 이것도 할 필요가 없음
    for i in range(len(first)):
        if max_value < first[i]:
            max_value = first[i]
            x = i
            y = 0

        
    d[0] = max_value

    max = 0                           # x값 받다가 실패함
    for i in range(1, m):
        C = max(data2[x-1][i], data2[x][i], data2[x+1][i])
        
        d[i] = d[i-1] + C



    x값만 받아오면 되는데 x값을 못받아옴..
    
    
    '''    