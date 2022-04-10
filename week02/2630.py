'''
문제 : 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램 작성

입력 : N (2,4,8,16,32,64,128) // 색종이의 각 가로줄의 정사각형 칸들의 색이 윗줄부터 차례로 주어짐, 하얀색 0 파란색 1 숫자 사이에 빈칸이 하나씩 있음

출력 : 하얀색 색종이 // 파란색 색종이

조건 : 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복

분할먼저 해야하는데 --> 재귀적으로 구현하면 될 거 같음
정복  --> 나눴을 때, 하나씩 확인해주는 과정을 거치면 될 거 같음. 

'''

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

w = 0
b = 0

def recursive(size, x, y):
    
    global b, w


    num = data[x][y]
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            
            if num != data[i][j]:           #key point 시작 하는 값과 같은지만 보면 된다.
    
             recursive(size//2, x, y)
             recursive(size//2, x, y + size//2)
             recursive(size//2, x + size//2, y)
             recursive(size//2, x + size//2, y + size//2)
             return                         # return을 안하면 어떻게 되는지? i = 0, j = 2일 때 다 돌고 끝나야는데, 
                                            # 즉 for문이 끝나줘야하는데 더 돌아버리는 문제가 생긴다.
             
    if num == 0:
        w += 1
    else:
        b += 1
                 

recursive(n, 0, 0)

print(w)
print(b)


'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''