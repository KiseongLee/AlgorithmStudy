# 10분 : 문제 흐름 파악, LCS문제랑은 조금 다른 듯
# 10분 : 이중 포문으로 하면 되겠다 -> 근데 dp문제인데 dp테이블 안써도 되나?
# 10분 : 내가 생각하는 것을 코드로 써보고 -> dp문제니까 dp테이블 쓰는 풀이 보고 구현해보고 마무리하자라는 생각
# 10분 : 구현 조금 더 해보자
# 10분 : 구현했는데 반례 ..
'''
14
1 2 3 4 6 5 4 1 2 3 4 6 5 4
14
5 1 4 3 6 2 4 5 1 4 3 6 2 4
4
내답:1 2 3 4
정답:1 3 4 5 6
'''


n = int(input())
S = list(map(int, input().split()))
m = int(input())
A = list(map(int, input().split()))


x=0
y=0
ans = []
for i in range(n):
    for j in range(y, m):
        if S[i] == A[j]:
            if S[x] < S[i] or x == 0:
                x = i
                y = j
                ans.append(S[i])
            break

print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=" ")


# https://www.geeksforgeeks.org/longest-common-increasing-subsequence-lcs-lis/




# LIS
# dp[i] = i번째 까지 LIS의 수

n = int(input())

data = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp)
print(max(dp))

#LCS
X= [0]+list(input())
Y = [0] + list(input())

dp =[[0]*(len(Y)) for _ in range(len(X))]

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            dp[i][j] = dp[i-1][j-1]+1
            # j를 j-1로 만들어야 답이 된다. 왜??
            # ABAA / AABB를 넣어보면 된다
            # 세번 째, A가 들어갔을 때, 2가 되면 안되는데 j를 넣으면 되버린다. 그래서 문제가 생긴다.
            # 추가 됨과 동시에 더해줘야하는거지. 추가 됨과 동시에 더해준다!!
            
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
for i in range(len(dp)):
    print(dp[i])

print(dp[-1][-1])



def LCIS(Apos, Bpos, dp, back):
    
    if Apos == len(S)-1 or Bpos == len(S)-1:
        return 0
    
    ret = dp[Apos][Bpos]
    if ret != -1:
        return ret
        
    ret = 1
    back[Apos][Bpos] = i*1000 + j
    
    for i in range(Apos+1, n):
        if S[Apos] >= S[i]: continue
        for j in range(Bpos+1, m):
            if S[i] == A[j]:
                temp = LCIS(i, j) + 1
                if ret<temp:
                    ret = temp
                    
                break
            
    return ret

def trace(Apos, Bpos):
    if Apos == len(S)-1 or Bpos == len(A)-1:
        print(S[Apos])
        trace(back[Apos][Bpos]//1000, back[Apos][Bpos]%1000)

n = int(input())
S = list(map(int, input().split()))
m = int(input())
A = list(map(int, input().split()))

dp =[[0]*(len(S)) for _ in range(len(A))]
back =[[0]*(len(S)) for _ in range(len(A))]


result = 0 
start = -1

for i in range(n):
    for j in range(m):
        if S[i] == A[j]:
            temp = LCIS(i, j, dp, back)
            if result < temp:
                result = temp
                start = i*1000+j
            break

print(result)
if start != -1:
    trace(start//1000, start%1000)
    

# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kks227&logNo=220603373411