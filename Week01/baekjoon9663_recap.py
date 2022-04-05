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

def promising (i, col):                 # 유망함수 조건 // 조건1. 같은 열에 오지 못한다, 조건2. 같은 대각선에 오지 못한다.
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