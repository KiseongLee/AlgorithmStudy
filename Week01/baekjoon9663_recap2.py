
n = int(input())

queen = [0] * n             # 열의 위치를 받는 배열
count = 0                  # 경우의 수 count



def promising(x):           # 유망함수의 구현
    
    for i in range(x):          # x보다 작은 i에서 유망한지 체크
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:   # 열이 같으면 대각선이 같으면 False 출력
            return False
        
    return True             # 위의 조건이 아니면 True를 출력
    





def dfs(x):
    global count            # 경우의 수를 구하기 위해 count 전역 변수
    
    if x == n :             # 재귀 종료 조건 : x가 n과 같을 때, 즉 depth가 n이 되었다는 것은 모든 행에 퀸을 놓았다는 뜻이므로
                            # 경우의 수 체크 해줄 수 있음
        count += 1 
        return
    
    for i in range(n):      
        queen[x] = i        # x행에 퀸을 하나씩 놓는다
        if promising(x):    # 유망하다면
            dfs(x+1)        # 깊이 탐색 시작
            

dfs(0)                      # queen 배열을 n개만 받았으므로 0부터 시작
print(count)                # 답출력