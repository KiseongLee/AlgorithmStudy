
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