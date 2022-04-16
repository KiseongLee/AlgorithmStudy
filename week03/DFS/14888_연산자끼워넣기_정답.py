import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

operator = list(map(int, input().split()))

max = -1000000001
min = 1000000001

ans = []
def dfs(data, total, plus, minus, mul, div, idx):
    
    global max, min
    
    if idx >= n:
      if total > max:
         max = total
      if total < min:
         min = total
      
        
    

    else:
      
      if plus: dfs(data, total+data[idx], plus-1, minus, mul, div, idx+1)
      if minus: dfs(data, total-data[idx], plus, minus-1, mul, div, idx+1)
      if mul: dfs(data, total*data[idx], plus, minus, mul-1, div, idx+1)
      if div: dfs(data, int(total/data[idx]), plus, minus, mul, div-1, idx+1)
       
        

dfs(data, data[0], operator[0], operator[1], operator[2], operator[3], 1)
print(max, min, sep='\n')
