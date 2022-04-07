import sys
n = int(input())

value = list(map(int, input().split()))

oper = list(map(int, input().split()))

min_value = sys.maxsize
max_value = -sys.maxsize

def dfs(x, idx, plus, minus, mul, div):
    global min_value, max_value
    # 1. 재귀 종료 조건
    
    if idx == n:
        
        min_value = min(min_value, x)
        max_value = max(max_value, x)
    
    
    else:
     if plus: dfs(x+value[idx], idx+1 , plus-1, minus, mul, div)
     if minus: dfs(x-value[idx], idx+1, plus, minus-1, mul, div)
     if mul : dfs(x*value[idx], idx+1, plus, minus, mul-1, div)
     if div : dfs(int(x/value[idx]), idx+1, plus, minus, mul, div-1)
                
 
dfs(value[0], 1, oper[0], oper[1], oper[2], oper[3])
print(max_value)
print(min_value)
    