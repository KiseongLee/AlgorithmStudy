def w(a,b,c):
    
    if a<= 0 or b <= 0 or c<= 0:
       return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]
    # dp에 저장해 놓는 것 까진 이해함
    # dp[a][b][c]가 0이 아니라면 바로 뽑아내는 것을 생각하지 못했고
    
    
dp = [[[0]*21 for _ in range(21)] for _ in range(21)] 
# 3차원 받는 것을 헷갈려버림 / 20번까지만 받으면 된다는게 핵심

while True:
    a, b, c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        break
    
    w(a,b,c)
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
    # dp를 뽑아내면 안되고, 함수를 뽑아내야한다!!