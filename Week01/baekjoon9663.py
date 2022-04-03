# 백트래킹
# 임의의 집합에서 기준에 따라 원소의 순서를 선택
# n - Queens
# 임의의 집합(set) : 체스보드에 있는 n^2개의 가능한 위치
# 기준(criterion) : 새로 놓은 퀸이 다른 퀸을 위협할 수 없음
# 원소의 순서(sequence) : 퀸을 놓을 수 있는 n개의 위치

# 상태 공간 트리

# 기본 가정 : 같은 행(row)에는 퀸을 놓지 않는다.
# 유망 함수의 구현
# 같은 열이나 같은 대각선에 놓이는지를 확인하면된다.
# 조건1 : col[i] : i번째 행(row)에서 퀸이 놓여 있는 열(column)위치
#        col[k] : k번째 행(row)에서 퀸이 놓여 있는 열(column)위치
#        col[i] == col[k] 같은 열에 놓이게 되므로 유망하지 않다

# 조건2 : 왼쪽에서 위협하하는 퀸에 대해서, 열에서의 차이는 행에서의 차이와 같다
#        col[i] - col[k] == i - k
#        오른쪽에서 위협하는 퀸에 대해서, 열에서의 차이는 행에서의 차이의 마이너스와 같다.


n = int(input())

queen = [0] * n
result = 0

def promising(x):

    for i in range(x):
        if x > i :
         if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:
                return False
    
    return True


def dfs(x):

    if x == n:
        if n == 0:
                return
        else:
         global result
         result += 1
         return
    
    for i in range(n):
        queen[x] = i 
        if promising(x):
            dfs(x+1) 

dfs(0)
print(result)

# 위 식으로 pypy3로 문제 품

'''
import sys
def n_queens (i, col ):             # 확인하는 함수
    global count
    if n >= 15:
        return

    if (promising(i, col)):
        if (i == n):                # n은 depth이다. 그래서 i == n이라는 것은 가장 깊은 곳 까지 탐색했다는 것을 의미한다.
            count += 1              # 그런데 거기에서 promising 함수가 True이면 count를 해줄 수 있는 것이다.
            
        else:
            for j in range(1, n + 1):   # 위의 경우가 아니면 탐색을 해줘야한다.
                col[i + 1] = j          # 같은 행에는 올 수가 없다고 하니 col[i + 1]이 된 것이고, j값을 1씩 올려가며 탐색한다.
                n_queens(i+1, col)      

def promising (i, col):
    k = 1
    flag = True
    
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

n = int(sys.stdin.readline())
col = [0] * (n + 1)
count = 0

n_queens(0, col)

if n >= 15:
    pass
else:
    print(count)
'''
#---------------------------------------
#책 풀이 (not backtracking)
'''
pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:

    for j in range(8):
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i - j + 7]:
           pos[i] = j
           if i==7:
              put()
           else:
               flag_a[j] = flag_b[i+j] = flag_c[i - j + 7] = True
               set(i+1)
               flag_a[j] = flag_b[i+j] = flag_c[i - j + 7] = False

set(0)
'''
