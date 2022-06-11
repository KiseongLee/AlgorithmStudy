n, q = map(int, input().split())
data = list(map(int, input().split()))
rev = list(map(int, input().split()))
dp = [0] * n    # dp 테이블 만들어준다 -> 계산할 것을 다 담아주는 리스트



for j in range(n):
    dp[j] = data[j-3]*data[j-2]*data[j-1]*data[j]   # 값을 계산할 떄, 거꾸로 생각하자, 
                                                    # 그러면 배열의 인덱스를 넘어가는 것을 생각할 필요없음
            
ex_sum = sum(dp)                # 내가 원하는 값은 dp 테이블을 sum한 값 -> 여기서 부호 바뀌는 것만 바꿔주면됨
for idx in rev:                 # 바꿔야할 소 번호를 for문 돌린다                    
    for i in range(4):          # 4개씩 곱하니까 부호를 바꿔줘야할 dp테이블 내의 인덱스는 4개다
        new_idx = (idx-1+i)%n   # idx-1은 내가 바꿔줘야할 인덱스이고 여기서 0,1,2,3을 더하면 되는데 
                                # -> 값이 넘어가는 것들은 n으로 나눈 나머지로 체크하면 된다!! 유레카 
        dp[new_idx] = -dp[new_idx] # 그리고 dp테이블에 있는 것이 부호가 바뀐 것이니까 초기화해주고
        ex_sum+=2*dp[new_idx]       # 그 값을 2번 더해주면 전체 값이 바뀌게 되는 것
    print(ex_sum)               