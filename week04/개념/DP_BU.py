n = int(input())

d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1]=1
d[2]=1

# 피보나치 함수 반복문으로 구현

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
