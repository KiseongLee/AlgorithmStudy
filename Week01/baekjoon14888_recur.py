n = int(input())

data= list(map(int, input().split()))

oper= list(map(int, input().split()))

max = -987654231
min = 987654321

def backtrack(total, idx, plus, minus, mul, div):
    global max, min
    if idx >= n:
       if total > max:
            max = total
       if total < min :
           min = total
    
    else:
        if plus: backtrack(total+data[idx], idx+1, plus-1, minus, mul, div)
        if minus: backtrack(total-data[idx], idx+1, plus, minus-1, mul, div)
        if mul: backtrack(total*data[idx], idx+1, plus, minus, mul-1, div)
        if div : backtrack(int(total/data[idx]), idx+1, plus, minus, mul, div-1)

backtrack(data[0], 1, oper[0], oper[1], oper[2], oper[3])
print(max)
print(min)





'''
def f(s, idx, plus, minus, mul, div):
    global minV, maxV
    if idx >= N:
        minV = s if s < minV else minV
        maxV = s if s > maxV else maxV
    else:
        if plus: f(s+M[idx], idx+1, plus-1, minus, mul, div)
        if minus: f(s-M[idx], idx+1, plus, minus-1, mul, div)
        if mul: f(s*M[idx], idx+1, plus, minus, mul-1, div)
        if div: f(int(s/M[idx]), idx+1, plus, minus, mul, div-1)

N = int(input())
M = list(map(int, input().split()))
C = list(map(int, input().split()))
minV = 987654321
maxV = -987654321

f(M[0], 1, C[0], C[1], C[2], C[3])

print(maxV)
print(minV)
'''